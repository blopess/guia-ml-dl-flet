# Guia Prático ML & DL — MVP Flet

Aplicativo educacional offline feito em Python com Flet.

O app possui três telas:

1. **Preparação** — caminho do dado antes da modelagem.
2. **Modelos** — escolha do modelo por tipo de alvo.
3. **Métricas** — avaliação de sucesso em classificação.

Cada card pode ser expandido com detalhes, exemplos e fórmulas em Markdown.

---

## 1. Rodar localmente

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate

pip install --upgrade pip
pip install -e .
python src/main.py
```

---

## 2. Build APK local

```bash
flet build apk
```

O APK será gerado dentro da pasta `build/`.

---

## 3. Executar no GitHub Actions

### Passo 1 — Criar repositório

Crie um repositório no GitHub, por exemplo:

```text
guia-ml-dl-flet
```

### Passo 2 — Enviar os arquivos

Suba esta estrutura para o repositório:

```text
guia-ml-dl-flet/
├── .github/
│   └── workflows/
│       ├── build-android-apk.yml
│       └── build-web.yml
├── src/
│   ├── assets/
│   │   └── icon.png
│   └── main.py
├── .gitignore
├── pyproject.toml
└── README.md
```

### Passo 3 — Rodar o build do APK

No GitHub:

1. Abra o repositório.
2. Clique em **Actions**.
3. Escolha **Build Android APK**.
4. Clique em **Run workflow**.
5. Aguarde o processo terminar.
6. Baixe o arquivo em **Artifacts** com o nome `guia-ml-dl-apk`.

---

## 4. Observação importante

O GitHub Actions não abre visualmente o app Android. Ele executa o processo de build e entrega o APK como artefato para download.

Para testar visualmente antes, rode localmente:

```bash
python src/main.py
```

---

## 5. Build web opcional

Existe também um workflow chamado **Build Web Preview**.

Ele gera uma versão web do app como artefato, útil para validação rápida, mas o objetivo principal deste MVP é o APK Android.
