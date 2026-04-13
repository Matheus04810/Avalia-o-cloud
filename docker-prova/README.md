Questão 1

UN + && + \ → menos camadas:
Cada instrução RUN no Dockerfile cria uma nova layer. Ao encadear comandos com && (e quebrar linha com \), você executa vários passos em uma única instrução, portanto gera menos layers.
Impacto (cache e tamanho):
Menos layers → imagem geralmente menor (menos overhead e arquivos intermediários podem ser removidos no mesmo RUN).
Porém, o cache fica menos granular: se algo muda no comando encadeado, toda a layer é invalidada. Já múltiplos RUN podem reaproveitar melhor o cache em partes.
docker history:
Mostra as layers da imagem (tamanho e comandos). É chave para validar otimização: você vê se reduziu o número de layers e quais comandos geraram mais peso.
.dockerignore:
Evita enviar arquivos desnecessários no contexto de build, reduzindo tempo e risco de vazamento.
Exemplo: ignorar .git/, node_modules/ ou .env (credenciais).

Questão  2
Bridge padrão (bridge):
Containers se comunicam por IP, não por nome. Esses IPs são voláteis (mudam ao reiniciar/recriar containers), o que quebra conexões e dificulta configuração → ruim para produção.
Bridge customizada:
Possui DNS interno automático: containers se comunicam pelo nome do serviço/container, não pelo IP. Assim, mesmo que o IP mude, a resolução continua funcionando.
A padrão é inadequada em produção por depender de IP instável; a customizada resolve usando descoberta por nome (service discovery), tornando a rede mais estável e previsível.

Questão 3

Infraestrutura como Código (IaC) no Docker é descrever toda a “oficina” (ambiente, ferramentas, máquinas e processos) em arquivos versionados — como Dockerfile e docker-compose.yml — em vez de configurar tudo manualmente.
O Dockerfile define como montar cada “máquina” (imagem).
O docker-compose organiza como elas se conectam (rede, volumes, serviços).
a oficina pode ser recriada de forma idêntica, automática e previsível em qualquer lugar, eliminando dependência de configurações manuais e inconsistências.