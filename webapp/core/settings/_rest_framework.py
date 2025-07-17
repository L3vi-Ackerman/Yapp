class RestFrameworkSettings:
    REST_FRAMEWORK = {
        "DEFAULT_PERMISSION_CLASSES": [
            "rest_framework.permissions.IsAuthenticated",
        ],
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "rest_framework_simplejwt.authentication.JWTAuthentication",
        ),
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "PAGE_SIZE": 10,
        "PAGE_QUERY_PARAM": "page",
        "PAGE_SIZE_QUERY_PARAM": "page_size",
        "MAX_PAGE_SIZE": 100,
    }
