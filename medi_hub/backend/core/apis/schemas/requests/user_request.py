from typing import Optional
from datetime import datetime, timezone
from pydantic import EmailStr, ConfigDict, BaseModel, Field
from enum import Enum


class UserAddress(BaseModel):
    """Represents a user's address information.

    Attributes:
        street: Street address (e.g., "123 Main St").
        city: City name (e.g., "Springfield").
        state: State or province (e.g., "IL").
        postal_code: Postal or ZIP code (e.g., "62704").
        country: Country name (e.g., "USA").
    """

    street: str = Field(..., description="Street address")
    city: str = Field(..., description="City name")
    state: str = Field(..., description="State or province")
    postal_code: str = Field(..., description="Postal or ZIP code")
    country: str = Field(..., description="Country name")


class UserProfileUpdateRequest(BaseModel):
    """Represents the data that can be updated for an existing user.

    Attributes:
        first_name: User's given name.
        last_name: User's family name.
        mobile_number: User's primary contact phone number.
        user_address: Optional address information for the user.
    """

    first_name: Optional[str] = Field(None, description="User's first name")
    last_name: Optional[str] = Field(None, description="User's last name")
    mobile_number: Optional[str] = Field(None, description="User's mobile phone number")
    user_address: Optional[UserAddress] = Field(
        None, description="User's address information"
    )
    user_metdata: Optional[dict] = Field(
        None,
        description="Additional metadata about the user (e.g., preferences, settings)",
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Timestamp when the user record was last updated",
    )
