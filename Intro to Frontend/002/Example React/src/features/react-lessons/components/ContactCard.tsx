import type { Contact } from '../types'

type ContactCardProps = {
  contact: Contact
}

export function ContactCard({ contact }: ContactCardProps) {
  return (
    <article className="contact-card">
      <div>
        <h4>{contact.name}</h4>
        <p>{contact.email}</p>
      </div>
      <span>{contact.status}</span>
    </article>
  )
}
