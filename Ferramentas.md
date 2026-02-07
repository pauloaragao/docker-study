# Ferramentas de Segurança em Containers

## 1. Cosign

### Descrição
Cosign é uma ferramenta do projeto Sigstore que fornece assinatura criptográfica e verificação de imagens de container e artefatos. Ela integra-se com a infraestrutura de chave pública (PKI) moderna para proteger a segurança da cadeia de suprimentos.

### Funcionalidades Principais
- **Assinatura de imagens**: Assina digitalmente imagens de container
- **Verificação de identidade**: Suporta verificação sem chave (keyless) usando identidades baseadas em e-mail
- **Integração com Sigstore**: Utiliza a infraestrutura completa do Sigstore
- **Verificação de proveniência**: Garante que imagens vêm de fontes confiáveis

### Instalação

#### Com Go 1.20+
```bash
go install github.com/sigstore/cosign/v3/cmd/cosign@latest
```

#### Homebrew/Linuxbrew
```bash
brew install cosign
```

#### Arch Linux
```bash
pacman -S cosign
```

#### Alpine Linux
```bash
apk add cosign
```

#### GitHub Actions
```yaml
uses: sigstore/cosign-installer@main
```

#### Download Binário
```bash
curl -O -L "https://github.com/sigstore/cosign/releases/latest/download/cosign-linux-amd64"
sudo mv cosign-linux-amd64 /usr/local/bin/cosign
sudo chmod +x /usr/local/bin/cosign
```

### Verificação de Releases
Antes de usar um binário baixado do Cosign, é importante verificar sua autenticidade. O Cosign fornece métodos para verificação com chaves de artefato e verificação baseada em identidade.

---

## 2. Chainguard Images

### Descrição
Chainguard Images é um repositório de imagens de container mínimas e endurecidas, reconstruídas diariamente a partir do código-fonte. Focam em eliminação de vulnerabilidades (CVEs) e conformidade com padrões de segurança.

### Funcionalidades Principais
- **Imagens mínimas**: Reduzem significativamente a superfície de ataque
- **Reconstrução diária**: Imagens atualizadas automaticamente com patches de segurança
- **Variantes FIPS**: Imagens em conformidade com o Federal Information Processing Standard
- **Proveniência clara**: Transparência completa sobre o que está em cada imagem
- **SLA de remediação**: Garantia de correção de vulnerabilidades

### Estatísticas Principais
- **2.076 projetos** disponíveis
- **176.161 versões** diferentes
- **349.207 imagens** no total
- **520.593.713 manifests** de build

### Imagens Destacadas (Gratuitas)
- **Go**: Última versão v1.25.7
- **Node**: Última versão v25.6.0
- **Python**: Última versão 3.14.3 (com variante FIPS)
- **Ruby**: Última versão v4.0.1
- **Rust**: Última versão v1.93.0

### Exemplo de Valor
Usando apenas 5 imagens base (Go, Node, Python, Ruby, Rust) seria possível eliminar 1.136 vulnerabilidades, representando uma redução de 99,30%!

### Acesso
- **Diretório**: https://images.chainguard.dev/directory
- **Consultor de Security**: https://images.chainguard.dev/security
- **Console**: https://console.chainguard.dev/

---

## 3. Trivy

### Descrição
Trivy é um scanner de vulnerabilidades abrangente desenvolvido pela Aqua Security. Detecta vulnerabilidades, misconfigurações e segredos em imagens de container, sistemas de arquivos, repositórios de código e muito mais.

### Funcionalidades Principais
- **Scanner de vulnerabilidades**: Identifica CVEs em dependências
- **Scanner de misconfigurações**: Detecta problemas de configuração em IaC
- **Scanner de segredos**: Encontra credenciais e chaves expostas
- **SBOM (Software Bill of Materials)**: Gera inventário de componentes
- **VEX (Vulnerability Exploitability eXchange)**: Avalia exploitabilidade de vulnerabilidades
- **Conformidade**: Suporte para CIS Benchmarks e outros padrões

### Alvos de Scan Suportados
- **Container Images**: Imagens Docker e OCI
- **Filesystem**: Sistemas de arquivos
- **Rootfs**: Sistema de arquivos raiz
- **Code Repository**: Repositórios Git
- **Machine Image**: Imagens de máquinas virtuais
- **Kubernetes**: Clusters Kubernetes
- **SBOM**: Análise de Bills of Materials

### Instalação

#### Container Image (Oficial)
```bash
docker run -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image python:3.4-alpine
```

#### Debian/Ubuntu
```bash
sudo apt-get install wget gnupg
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor | sudo tee /usr/share/keyrings/trivy.gpg > /dev/null
echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb generic main" | sudo tee -a /etc/apt/sources.list.d/trivy.list
sudo apt-get update
sudo apt-get install trivy
```

#### RHEL/CentOS
```bash
cat << EOF | sudo tee -a /etc/yum.repos.d/trivy.repo
[trivy]
name=Trivy repository
baseurl=https://aquasecurity.github.io/trivy-repo/rpm/releases/\$basearch/
gpgcheck=1
enabled=1
gpgkey=https://aquasecurity.github.io/trivy-repo/rpm/public.key
EOF
sudo yum -y update
sudo yum -y install trivy
```

#### Homebrew
```bash
brew install trivy
```

#### Via Script de Instalação
```bash
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sudo sh -s -- -b /usr/local/bin
```

#### Arch Linux
```bash
sudo pacman -S trivy
```

#### Windows
Baixar arquivo `trivy_x.xx.x_windows-64bit.zip` da [página de releases](https://github.com/aquasecurity/trivy/releases/)

### Integração com CI/CD
- **GitHub Actions**: Ação nativa disponível no Marketplace
- **GitLab CI**: Exemplo com `apk add --update cosign`
- **CircleCI, Travis CI, Bitbucket Pipelines**: Suportados
- **AWS CodePipeline**: Integração disponível

### Cobertura de Segurança
Trivy suporta scanning de múltiplos SO e linguagens:

**Sistemas Operacionais:**
- Alpine Linux, Debian, Ubuntu
- CentOS, Red Hat, Rocky Linux
- Amazon Linux, Azure Linux
- Chainguard, Wolfi, e outros

**Linguagens:**
- Go, Python, Java, Node.js
- Ruby, Rust, .NET, PHP
- C/C++, Dart, Elixir, Julia, Swift

**Infrastructure as Code:**
- Terraform, Kubernetes, Dockerfile
- Helm Charts, CloudFormation, Ansible
- Azure ARM Templates

---

## Comparação e Uso Combinado

### Fluxo de Trabalho Recomendado

1. **Desenvolvimento com Chainguard Images**: Use imagens base Chainguard para reduzir vulnerabilidades desde o início
2. **Build com Trivy**: Escaneie sua imagem com Trivy antes de fazer push
3. **Assinatura com Cosign**: Assine imagens verificadas com Cosign
4. **Verificação no Runtime**: Use Cosign para verificar integridade de imagens em produção

### Exemplo de Pipeline Seguro
```
Chainguard Base Image
         ↓
    Build Image
         ↓
    Trivy Scan
         ↓
    Cosign Sign (se aprovado)
         ↓
    Push para Registry
         ↓
    Cosign Verify (on deploy)
```

---

## Recursos Adicionais

- **Sigstore**: https://docs.sigstore.dev/
- **Chainguard**: https://www.chainguard.dev/
- **Trivy**: https://trivy.dev/
- **Supply Chain Security 101**: https://www.chainguard.dev/supply-chain-security-101
