# PixelTag API
PixelTag API

## Dependências

## Config

## Endpoints

### POST /user

Cria um usuário. O conteúdo do request deverá ser com código ```201 Created``` e retornar um objeto JSON com o conteúdo no seguinte formato. Caso já exista um usuário com o mesmo id retornar código ```409 Conflict```

Requisição:

```curl -I -X POST -H "Content-Type:application/json" http://<host>[:<port>]/:user -d '{"id":"rambo"}'```

Resposta:

```
{
    "id": "rambo"
}
```

### POST /tag/:user

Cria uma nova tag no sistema. O conteúdo do request deverá ser com código ```201 Created``` e retornar um objeto JSON com o conteúdo no seguinte formato. Caso já exista com o mesmo id retornar código ```409 Conflict```.

Requisição:

```curl -I -X POST -H "Content-Type:application/json" http://<host>[:<port>]/:user -d '{"id":"rambo"}'```

Resposta:

```
{
    "tagurl": "http://<host>[:<port>]/tag/:user/:tagid"
}
```

### GET /tag/:user/:tag

Registra os dados da requisição, e retorna uma imagem de 1px.

### GET /stats/:user/:tag

## Tests


