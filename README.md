# Raspagem de Notícias do Náutico

Este é um script Python que realiza a raspagem (web scraping) de notícias do Náutico no portal ge.globo.com.

## 🚀 Funcionalidades

- Acessa automaticamente o site do Náutico no ge.globo.com
- Coleta as 10 notícias mais recentes
- Extrai título e link de cada notícia
- Salva as informações em um arquivo de texto formatado

## 📋 Pré-requisitos

- Python 3.x
- Google Chrome instalado
- ChromeDriver compatível com sua versão do Chrome
- Bibliotecas Python:
  - selenium
  - webdriver_manager

## 🔧 Instalação

1. Clone este repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd raspagemNoticias
```

2. Instale as dependências:
```bash
pip install selenium webdriver_manager
```

3. Baixe o ChromeDriver:
   - Acesse https://chromedriver.chromium.org/downloads
   - Baixe a versão compatível com seu Chrome
   - Extraia o arquivo `chromedriver.exe` para a pasta `driver` do projeto

## 🎯 Como Usar

1. Certifique-se de que o ChromeDriver está no caminho correto:
   - O arquivo deve estar em: `C:\Users\Educação\Pictures\raspagemNoticias\driver\chromedriver.exe`

2. Execute o script:
```bash
python noticias.py
```

3. O resultado será salvo em `noticias_nautico.txt`

## 📁 Estrutura do Projeto

```
raspagemNoticias/
├── driver/
│   └── chromedriver.exe
├── noticias.py
└── README.md
```

## ⚠️ Observações

- O script pode precisar de ajustes se o site do ge.globo.com mudar sua estrutura
- Certifique-se de ter uma conexão estável com a internet
- O ChromeDriver deve ser atualizado quando o Chrome for atualizado

## 🤝 Contribuindo

Sinta-se à vontade para contribuir com melhorias no código!

## 📝 Licença

Este projeto está sob a licença MIT. 