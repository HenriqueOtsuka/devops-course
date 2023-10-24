Quando definido como always, o contêiner será reiniciado automaticamente, não importa qual seja o motivo do seu término. Isso inclui o término do contêiner por falhas ou pelo comando docker stop.
Se você reiniciar o sistema, o contêiner também será iniciado automaticamente.


Similar ao always, mas com uma exceção: se o contêiner for parado manualmente por um usuário (por exemplo, através do comando docker stop ou docker-compose down), ele não será reiniciado automaticamente, mesmo após uma reinicialização do sistema.