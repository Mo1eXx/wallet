# проект Wallets
___

## Для запуска проекта:
- скачать файл ```docker-compose.production.yml```
- создать файл ```.env``` на основе ```.env.example```
- запустить командой ```sudo docker compose -f docker-compose.production.yml up```
- выполнить миграцию ```sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate```
- собрать статику ```sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic```
- скопировать статику ```sudo docker compose -f docker-compose.production.yml exec backend cp -r /app/collected_static/. /backend_static/static/ ```
---
 Приложение доступно по адресу ```http://localhost:8000/api/v1/wallets/```
 
При POST запросе будет создан пустой Wallet с уникальным ID и балансом 0.00

## Для изменения данных:
POST ```http://localhost:8000/api/v1/<WALLET_UUID>/operation```

С телом 
```
{

operation_type: deposit or withdraw,

amount: 1000

}
```
Будет выполнена логика по изменению счёта

Также доступен просмотр баланса

GET ```http://localhost:8000/api/v1/<WALLET_UUID>/```
___

### Проект построен при использовании технологий:
- Python
- Django
- PostgreSQL
- Docker
- Docker-compose

### Автор [Артемий](hhtps://github.com/Mo1eXx).