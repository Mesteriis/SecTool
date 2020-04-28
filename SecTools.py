"""
----------------------------------------------------------------------------------------------------------------
Данный проект создан исключительно d ознакомительных в целях и для разбора технологии генерации пар,
любое использования в данного пакета возлагает ответственность на использующего.
Данный пакет распространяется как есть, автор снимает с себя ответственность за любые последствия использования

This project was created exclusively for informational purposes with a view to analyzing the technology of
generating pairs, any use in this package blames the user. This package is distributed as is,
the author disclaims responsibility for any consequences of using
-----------------------------------------------------------------------------------------------------------------
for use:
    hack_algo.hack_login_password_random(
        generators.generate_logins,
        generators.generate_popular_passwords,
        requesters.request_local_server
    )
for test
server.app.run()

"""
from components import hack_algo, generators, requesters
from testServer import server

print(__doc__)


