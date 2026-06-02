import { useCallback, useEffect, useMemo, useState } from "react";
import type { FormEvent } from "react";
import heroImage from "../../assets/hero.png";
import { CodeBlock } from "../../shared/components/CodeBlock";
import { Section } from "../../shared/components/Section";
import { StatusMessage } from "../../shared/components/StatusMessage";
import { useLocalStorage } from "../../shared/hooks/useLocalStorage";
import { ContactCard } from "../react-lessons/components/ContactCard";
import { starterContacts } from "../react-lessons/data";
import type { Contact } from "../react-lessons/types";
import { MetricCard } from "./components/MetricCard";

const componentCode = `type MetricCardProps = {
  label: string
  value: string | number
  detail: string
}

function MetricCard({ label, value, detail }: MetricCardProps) {
  return (
    <article className="metric-card">
      <span>{label}</span>
      <strong>{value}</strong>
      <p>{detail}</p>
    </article>
  )
}`;

const hooksCode = `const [contacts, setContacts] = useState(starterContacts)

const filteredContacts = useMemo(() => {
  return contacts.filter((contact) => contact.name.includes(search))
}, [contacts, search])

useEffect(() => {
  document.title = \`Dashboard (\${contacts.length})\`
}, [contacts.length])

const handlePromoteContact = useCallback((contactId: number) => {
  setContacts((current) => current.map((contact) => {
    return contact.id === contactId ? { ...contact, status: "Customer" } : contact
  }))
}, [])`;

function getNextStatus(status: Contact["status"]) {
  if (status === "Lead") {
    return "Follow-up";
  }

  if (status === "Follow-up") {
    return "Customer";
  }

  return "Customer";
}

export function DashboardPage() {
  const [contacts, setContacts] = useState<Contact[]>(starterContacts);
  const [search, setSearch] = useLocalStorage("fde-dashboard-search", "");
  const [name, setName] = useState("Arjun Nair");
  const [email, setEmail] = useState("arjun@example.com");
  const [status, setStatus] = useState<Contact["status"]>("Lead");
  const [selectedContactId, setSelectedContactId] = useState<number | null>(
    starterContacts[0].id,
  );
  const [formError, setFormError] = useState("");

  const statusCounts = useMemo(() => {
    return contacts.reduce(
      (counts, contact) => {
        counts[contact.status] += 1;
        return counts;
      },
      { Lead: 0, Customer: 0, "Follow-up": 0 } satisfies Record<
        Contact["status"],
        number
      >,
    );
  }, [contacts]);

  const filteredContacts = useMemo(() => {
    const query = search.toLowerCase().trim();

    if (!query) {
      return contacts;
    }

    return contacts.filter((contact) => {
      return (
        contact.name.toLowerCase().includes(query) ||
        contact.email.toLowerCase().includes(query) ||
        contact.status.toLowerCase().includes(query)
      );
    });
  }, [contacts, search]);

  const selectedContact = useMemo(() => {
    return (
      contacts.find((contact) => contact.id === selectedContactId) ??
      contacts[0]
    );
  }, [contacts, selectedContactId]);

  useEffect(() => {
    document.title = `Dashboard (${contacts.length}) | FDE React Demo`;
  }, [contacts.length]);

  const handleAddContact = useCallback(
    (event: FormEvent<HTMLFormElement>) => {
      event.preventDefault();

      if (!name.trim() || !email.trim()) {
        setFormError("Name and email are required.");
        return;
      }

      const nextContact: Contact = {
        id: Date.now(),
        name: name.trim(),
        email: email.trim(),
        status,
      };

      setContacts((currentContacts) => [nextContact, ...currentContacts]);
      setSelectedContactId(nextContact.id);
      setName("");
      setEmail("");
      setStatus("Lead");
      setFormError("");
    },
    [email, name, status],
  );

  const handlePromoteContact = useCallback((contactId: number) => {
    setContacts((currentContacts) => {
      return currentContacts.map((contact) => {
        if (contact.id !== contactId) {
          return contact;
        }

        return { ...contact, status: getNextStatus(contact.status) };
      });
    });
    setSelectedContactId(contactId);
  }, []);

  const dashboardMetrics = [
    {
      label: "Contacts",
      value: contacts.length,
      detail: "Managed in useState",
    },
    {
      label: "Leads",
      value: statusCounts.Lead,
      detail: "Calculated with useMemo",
    },
    {
      label: "Follow-ups",
      value: statusCounts["Follow-up"],
      detail: "Derived from contact list",
    },
    {
      label: "Customers",
      value: statusCounts.Customer,
      detail: "Updated by useCallback handler",
    },
  ];

  return (
    <>
      <header className="page-hero dashboard-hero">
        <div>
          <span className="eyebrow">Main Dashboard</span>
          <h1>Frontend Learning CRM</h1>
          <p>
            A small dashboard that demonstrates components, props, controlled
            forms, state, derived data, side effects, memoization, and callback
            functions.
          </p>
        </div>
        <img
          src={heroImage}
          alt="React dashboard preview"
          className="hero-image"
        />
      </header>

      <section className="metric-grid" aria-label="Dashboard metrics">
        {dashboardMetrics.map((metric) => (
          <MetricCard
            key={metric.label}
            label={metric.label}
            value={metric.value}
            detail={metric.detail}
          />
        ))}
      </section>

      <Section
        id="dashboard-components"
        eyebrow="001"
        title="Component And Props"
        description="The dashboard uses small components like MetricCard and ContactCard to receive data through props."
      >
        <div className="two-column">
          <div className="demo-panel">
            <h3>Selected Contact</h3>
            {selectedContact ? (
              <>
                <ContactCard contact={selectedContact} />
                <button
                  type="button"
                  onClick={() => {
                    console.log("Rendering App component");
                    handlePromoteContact(selectedContact.id);
                  }}
                >
                  Move Status Forward
                </button>
              </>
            ) : (
              <StatusMessage tone="warning">No contact selected.</StatusMessage>
            )}
          </div>
          <CodeBlock>{componentCode}</CodeBlock>
        </div>
      </Section>

      <Section
        id="dashboard-state"
        eyebrow="002"
        title="useState, useEffect, useMemo, useCallback"
        description="The dashboard stores user input, updates the document title, derives metrics, and keeps handlers stable."
      >
        <div className="two-column">
          <form className="contact-form" onSubmit={handleAddContact}>
            <h3>Add Contact</h3>
            <label htmlFor="contact-name">Name</label>
            <input
              id="contact-name"
              value={name}
              onChange={(event) => setName(event.target.value)}
              placeholder="Enter contact name"
            />

            <label htmlFor="contact-email">Email</label>
            <input
              id="contact-email"
              type="email"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
              placeholder="Enter contact email"
            />

            <label htmlFor="contact-status">Status</label>
            <select
              id="contact-status"
              value={status}
              onChange={(event) =>
                setStatus(event.target.value as Contact["status"])
              }
            >
              <option>Lead</option>
              <option>Follow-up</option>
              <option>Customer</option>
            </select>

            <button type="submit">Add Contact</button>
            {formError && (
              <StatusMessage tone="error">{formError}</StatusMessage>
            )}
          </form>

          <div>
            <label htmlFor="contact-search">Search Contacts</label>
            <input
              id="contact-search"
              value={search}
              onChange={(event) => setSearch(event.target.value)}
              placeholder="Search name, email, or status"
            />
            <div className="contact-list">
              {filteredContacts.length === 0 ? (
                <StatusMessage tone="warning">
                  No contacts match this search.
                </StatusMessage>
              ) : (
                filteredContacts.map((contact) => (
                  <button
                    className="contact-button"
                    type="button"
                    key={contact.id}
                    onClick={() => setSelectedContactId(contact.id)}
                  >
                    <ContactCard contact={contact} />
                  </button>
                ))
              )}
            </div>
          </div>
        </div>
      </Section>

      <Section
        id="dashboard-hook-code"
        eyebrow="003"
        title="Hooks Code"
        description="This is the exact pattern used in the dashboard page."
      >
        <CodeBlock>{hooksCode}</CodeBlock>
      </Section>
    </>
  );
}
