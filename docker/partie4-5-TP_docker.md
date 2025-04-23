J'ai réaliser les différents points demandé depuis le terminal et j'ai effectué des vérifications depuis Docker Desktop.

PS C:\Users\Titi\mars-rover\docker\image2-html> docker run -d -p 8080:80 -v ${PWD}/index.html:/usr/share/nginx/html/index.html nginx

PS C:\Users\Titi\mars-rover\docker\image2-html> docker stop 6d6101c04bee 

PS C:\Users\Titi\mars-rover\docker\image2-html> docker run -d -p 8080:80 -v ${PWD}/index.html:/usr/share/nginx/html/index.html nginx

PS C:\Users\Titi\mars-rover\docker\image2-html> docker network create tp-net

docker run -dit --name conteneur1 --network tp-net alpine sh
docker run -dit --name conteneur2 --network tp-net alpine sh

docker exec -it conteneur1 sh
ping conteneur2