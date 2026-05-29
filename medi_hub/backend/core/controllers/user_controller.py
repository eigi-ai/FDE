from fastapi import HTTPException, status
from core import logger
from core.cruds.auth_crud import CRUDAuth

logging = logger(__name__)


class UserController:
    """
    Controller for user-related operations, such as fetching user details, updating user information, etc.
    """

    def __init__(self):
        self.crud_auth = CRUDAuth()

    async def list_users(self):
        """
        Fetch a list of all users.

        Returns:
            A list of user details.

        Raises:
            HTTPException with status code 500 for any unexpected errors.
        """
        try:
            logging.info(f"Executing UserController.list_users function")
            result = await self.crud_auth.get_all()
            return result
        except HTTPException:
            raise
        except Exception as error:
            logging.error(f"Error in UserController.list_users function: {error}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(error),
            )

    async def get_user_by_id(self, id: str):
        """
        Fetch user details by user ID.

        Args:
            id: The ObjectId of the user to fetch.

        Returns:
            User details if found.

        Raises:
            HTTPException with status code 404 if the user is not found.
            HTTPException with status code 500 for any unexpected errors.
        """
        try:
            logging.info(
                f"Executing UserController.get_user_by_id function for user ID {id}"
            )
            result = await self.crud_auth.get_by_id(id=id)
            return result
        except HTTPException:
            raise
        except Exception as error:
            logging.error(
                f"Error in UserController.get_user_by_id function for user ID {id}: {error}"
            )
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(error),
            )

    async def update_user_by_id(self, id: str, request: dict):
        """
        Update user details by user ID.

        Args:
            id: The ObjectId of the user to update.
            request: A dictionary containing the fields to update.

        Returns:
            Updated user details if the update is successful.

        Raises:
            HTTPException with status code 404 if the user is not found.
            HTTPException with status code 500 for any unexpected errors.
        """
        try:
            logging.info(
                f"Executing UserController.update_user_by_id function for user ID {id}"
            )
            user = await self.crud_auth.get_by_id(id=id)
            if not user:
                logging.warning(f"User with ID {id} not found for update")
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found",
                )
            update_result = await self.crud_auth.update(id=id, obj_in=request)
            if not update_result:
                logging.warning(f"User with ID {id} not found for update")
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found",
                )
            return update_result
        except HTTPException:
            raise
        except Exception as error:
            logging.error(
                f"Error in UserController.update_user_by_id function for user ID {id}: {error}"
            )

    async def delete_user_by_id(self, id: str):
        """
        Delete a user by user ID.

        Args:
            id: The ObjectId of the user to delete.

        Returns:
            A success message if deletion is successful.

        Raises:
            HTTPException with status code 404 if the user is not found.
            HTTPException with status code 500 for any unexpected errors.
        """
        try:
            logging.info(
                f"Executing UserController.delete_user_by_id function for user ID {id}"
            )
            user = await self.crud_auth.get_by_id(id=id)
            if not user:
                logging.warning(f"User with ID {id} not found for deletion")
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found",
                )
            delete_result = await self.crud_auth.delete(id=id)
            if not delete_result:
                logging.warning(f"User with ID {id} not found for deletion")
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found",
                )
            return {"message": "User deleted successfully"}
        except HTTPException:
            raise
        except Exception as error:
            logging.error(
                f"Error in UserController.delete_user_by_id function for user ID {id}: {error}"
            )
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(error),
            )
