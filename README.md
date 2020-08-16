# ビルド
```bash
pushd app

docker build -t miyanonchi/myddns:v0.1.0 .
docker push miyanonchi/myddns:v0.1.0

popd
```

# ビルド (buildx)
```bash
pushd app

docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7,linux/arm/v8 -t miyanonchi/myddns:v0.1.0 --push .

popd
```

# 実行
```bash
docker-compose up -d

# log確認
docker-compose logs -f app
```

# テストの実行
```bash
docker-compose -f docker-compose.yml -f docker-compose-develop.yml up -d
docker-compose -f docker-compose.yml -f docker-compose-develop.yml logs app
```

