from typing import Optional, Union


class database:
    def __init__(
        self,
        dialect: str,
        user: str,
        host: str,
        password: str,
        database: str,
        port: Optional[Union[str, int]] = "",
    ):
        if not port:
            if dialect == "mysql":
                port = 3306
            elif dialect == "postgres":
                port = 5432
            else:
                raise ValueError("invalid default `port` for unrecognized `dialect`")
        if port is str and not port.isnumeric():
            raise ValueError("`port` must have a numeric value")

        self.connection_url = (
            f"{dialect}://{user}:{password}" f"@{host}:{port}/{database}"
        )
