from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from core import logger
from commons.auth import decodeJWT
from core.apis.schemas.responses.user_response import UserResponse, UsersListResponse
from core.apis.schemas.requests.auth_request import UserUpdateRequest
from core.controllers.user_controller import UserController
from core.apis.schemas.requests.user_request import UserProfileUpdateRequest

user_router = APIRouter()
logging = logger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/login")


@user_router.get("/v1/users", response_model=UsersListResponse)
async def get_users(token: str = Depends(oauth2_scheme)):
    """
    Endpoint to fetch a list of users. This is a protected route that requires authentication.

    Args:
        token: The JWT token provided in the Authorization header.
    Returns:
        A list of users if the token is valid.
    Raises:
        HTTPException with status code 401 if the token is invalid or expired.
        HTTPException with status code 500 for any unexpected errors.
    """
    try:
        logging.info(f"Calling /v1/users endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if not authenticated_user_details:
            logging.warning(f"Invalid or expired token provided for fetching users")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token",
            )
        if authenticated_user_details.get("user_role") != "ADMIN":
            logging.warning(
                f"Unauthorized access attempt to /v1/users endpoint by user ID {authenticated_user_details.get('id')}"
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource",
            )
        result = await UserController().list_users()
        response = UsersListResponse(
            message="Users fetched successfully",
            users=[
                UserResponse(
                    **{
                        **user.model_dump(exclude={"password"}),
                        "id": str(user.id),
                    }
                )
                for user in result
            ],
        )
        return response.model_dump()
    except HTTPException as httperror:
        logging.error(f"Error in /v1/users endpoint: {httperror}")
        raise httperror
    except Exception as error:
        logging.error(f"Error in /v1/users endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error),
        )


@user_router.get("/v1/users/{user_id}", response_model=UserResponse)
async def get_user_by_id(user_id: str, token: str = Depends(oauth2_scheme)):
    """
    Endpoint to fetch a user by their ID. This is a protected route that requires authentication.

    Args:
        user_id: The ID of the user to fetch.
        token: The JWT token provided in the Authorization header.
    Returns:
        The user details if the token is valid and the user exists.
    Raises:
        HTTPException with status code 401 if the token is invalid or expired.
        HTTPException with status code 404 if the user is not found.
        HTTPException with status code 500 for any unexpected errors.
    """
    try:
        logging.info(f"Calling /v1/users/{user_id} endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if not authenticated_user_details:
            logging.warning(
                f"Invalid or expired token provided for fetching user by ID"
            )
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token",
            )
        if (
            authenticated_user_details.get("id") != user_id
            and authenticated_user_details.get("user_role") != "ADMIN"
        ):
            logging.warning(
                f"User ID {authenticated_user_details.get('id')} attempted to access user ID {user_id} details without permission"
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource",
            )
        result = await UserController().get_user_by_id(id=user_id)
        if not result:
            logging.warning(f"User with ID {user_id} not found")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        response = UserResponse(
            **{
                **result.model_dump(exclude={"password"}),
                "id": str(result.id),
            }
        )
        return response.model_dump()
    except HTTPException as httperror:
        logging.error(f"Error in /v1/users/{user_id} endpoint: {httperror}")
        raise httperror
    except Exception as error:
        logging.error(f"Error in /v1/users/{user_id} endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error),
        )


@user_router.patch("/v1/users/{user_id}", response_model=UserResponse)
async def update_user_by_id(
    user_id: str, request: UserUpdateRequest, token: str = Depends(oauth2_scheme)
):
    """
    Endpoint to update a user's details by their ID. This is a protected route that requires authentication.

    Args:
        user_id: The ID of the user to update.
        request: The UserUpdateRequest containing the fields to update.
        token: The JWT token provided in the Authorization header.
    Returns:
        The updated user details if the token is valid and the update is successful.
    Raises:
        HTTPException with status code 401 if the token is invalid or expired.
        HTTPException with status code 404 if the user is not found.
        HTTPException with status code 500 for any unexpected errors.
    """
    try:
        logging.info(f"Calling PATCH /v1/users/{user_id} endpoint")
        request = request.model_dump(exclude_unset=True)
        authenticated_user_details = decodeJWT(token=token)
        if not authenticated_user_details:
            logging.warning(
                f"Invalid or expired token provided for updating user by ID"
            )
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token",
            )
        if authenticated_user_details.get("user_role") != "ADMIN":
            logging.warning(
                f"Unauthorized update attempt to user ID {user_id} by user ID {authenticated_user_details.get('id')}"
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action",
            )
        result = await UserController().update_user_by_id(id=user_id, request=request)
        if not result:
            logging.warning(f"User with ID {user_id} not found for update")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        response = UserResponse(
            **{
                **result.model_dump(exclude={"password"}),
                "id": str(result.id),
            }
        )
        return response.model_dump()
    except HTTPException as httperror:
        logging.error(f"Error in PATCH /v1/users/{user_id} endpoint: {httperror}")
        raise httperror
    except Exception as error:
        logging.error(f"Error in PATCH /v1/users/{user_id} endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error),
        )


@user_router.patch("/v1/users/{user_id}/profile")
async def update_user_profile_by_id(
    user_id: str, request: UserProfileUpdateRequest, token: str = Depends(oauth2_scheme)
):
    """
    Endpoint to update a user's profile details by their ID. This is a protected route that requires authentication.

    Args:
        user_id: The ID of the user to update.
        request: The UserProfileUpdateRequest containing the profile fields to update.
        token: The JWT token provided in the Authorization header.
    Returns:
        The updated user details if the token is valid and the update is successful.
    Raises:
        HTTPException with status code 401 if the token is invalid or expired.
        HTTPException with status code 404 if the user is not found.
        HTTPException with status code 500 for any unexpected errors.
    """
    try:
        logging.info(f"Calling PATCH /v1/users/{user_id}/profile endpoint")
        request = request.model_dump(exclude_unset=True)
        authenticated_user_details = decodeJWT(token=token)
        if not authenticated_user_details:
            logging.warning(
                f"Invalid or expired token provided for updating user profile by ID"
            )
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token",
            )
        if (
            authenticated_user_details.get("id") != user_id
            and authenticated_user_details.get("user_role") != "ADMIN"
        ):
            logging.warning(
                f"User ID {authenticated_user_details.get('id')} attempted to update user ID {user_id} profile without permission"
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action",
            )
        result = await UserController().update_user_by_id(id=user_id, request=request)
        if not result:
            logging.warning(f"User with ID {user_id} not found for profile update")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        response = UserResponse(
            **{
                **result.model_dump(exclude={"password"}),
                "id": str(result.id),
            }
        )
        return response.model_dump()
    except HTTPException as httperror:
        logging.error(
            f"Error in PATCH /v1/users/{user_id}/profile endpoint: {httperror}"
        )
        raise httperror
    except Exception as error:
        logging.error(f"Error in PATCH /v1/users/{user_id}/profile endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error),
        )


@user_router.delete("/v1/users/{user_id}")
async def delete_user_by_id(user_id: str, token: str = Depends(oauth2_scheme)):
    """
    Endpoint to delete a user by their ID. This is a protected route that requires authentication.

    Args:
        user_id: The ID of the user to delete.
        token: The JWT token provided in the Authorization header.
    Returns:
        A success message if the deletion is successful.
    Raises:
        HTTPException with status code 401 if the token is invalid or expired.
        HTTPException with status code 404 if the user is not found.
        HTTPException with status code 500 for any unexpected errors.
    """
    try:
        logging.info(f"Calling DELETE /v1/users/{user_id} endpoint")
        authenticated_user_details = decodeJWT(token=token)
        if not authenticated_user_details:
            logging.warning(
                f"Invalid or expired token provided for deleting user by ID"
            )
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token",
            )
        if authenticated_user_details.get("user_role") != "ADMIN":
            logging.warning(
                f"Unauthorized delete attempt to user ID {user_id} by user ID {authenticated_user_details.get('id')}"
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action",
            )
        result = await UserController().delete_user_by_id(id=user_id)
        if not result:
            logging.warning(f"User with ID {user_id} not found for deletion")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
        return {"message": "User deleted successfully"}
    except HTTPException as httperror:
        logging.error(f"Error in DELETE /v1/users/{user_id} endpoint: {httperror}")
        raise httperror
    except Exception as error:
        logging.error(f"Error in DELETE /v1/users/{user_id} endpoint: {error}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(error),
        )
