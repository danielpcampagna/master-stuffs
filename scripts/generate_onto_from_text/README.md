Para utilizar o [LinkML](), siga os passos:

Assumindo que você tenha construido sua ontologia num formato RDF, siga os passos 1-2 para converter para um formato aceito pelo LinkML.

1. Utilize o `[robot]()` para converter de um formato RDF qualquer para OFN:

```bash
robot convert -i gdprov_v0.8.ttl - gdprov.ofn
```

2. Em seguida, use o `[schema-automator]()` para converter do formto OFN para o formato Yaml do LinkML:

```bash
pip install schema-automator
schemauto import-owl gdprov.ofn -o gdprov2.yml
```

3. Por fim, faça uso do LinkML a partir dos seus dados.
