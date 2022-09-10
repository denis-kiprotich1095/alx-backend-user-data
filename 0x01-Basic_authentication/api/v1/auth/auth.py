#!/usr/bin/env python3
"""Auth class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False - path and excluded_paths"""
        if path is None or path not in excluded_paths:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        path_a = '/api/v1/status/'
        for i in excluded_paths:
            for j in range(0, len(i)):
                if j.endswith('/') and j.startswith(path_a, 0, 14):
                    return False
        if i == '/api/v1/status/' in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """returns None - request"""
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request will be the Flask request object"""
        return (None)