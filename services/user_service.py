from typing import List, Tuple

from entities.user import User

from abc import ABC, abstractmethod

class UserService(ABC):
    @abstractmethod
    def add_user(self, user: User) -> User:
        pass

    @abstractmethod
    def get_single_user(self, user_id: int) -> User:
        pass

    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass

    @abstractmethod
    def update_user(self, user: User) -> User:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        pass

    @abstractmethod
    def login(self, username: str, password: str) -> Tuple[str, int]:
        pass