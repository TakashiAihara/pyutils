def make_url(
    rdbms: str,
    database: str,
    driver: str = "",
    user: str = "",
    password: str = "",
    host: str = "localhost",
    port: str = "",
    optional: str = "",
):
    return (
        f"{rdbms}"
        f'{"+"+driver if bool(driver) else ""}'
        f"://"
        f'{user if bool(user) else ""}'
        f'{":"+password if bool(password) else ""}'
        f'{"@" if bool(user) else ""}'
        f'{host if (rdbms != "sqlite") else ""}'
        f'{":"+str(port) if bool(port) else ""}'
        f'{"/"}'
        f"{database}"
        f'{"?"+optional if bool(optional) else ""}'
    )
