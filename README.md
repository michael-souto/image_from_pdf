## Extrator de Imagens de PDFs
Este projeto permite:
- Rasterizar (converter em imagem) cada página de um arquivo PDF a 300 DPI.
- Extrair todas as imagens incorporadas nas páginas.
- Extrair componentes individuais de imagem identificados na camada de layout do PDF.
- Salvar todas as imagens extraídas em uma estrutura de pastas organizada.

## Pré-Requisitos
- Python 3.7+ instalado no sistema.
- Recomenda-se utilizar um ambiente virtual (venv) para evitar conflitos de dependências.

## Bibliotecas Necessárias:
- PyMuPDF (fitz) para manipulação de PDFs.
- Pillow para manipulação e salvamento de imagens.

## Instalação
Clonar o Repositório
Use o Git para clonar o repositório:
```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
```

- Em seguida, entre no diretório do projeto:
```bash
cd seu_repositorio
Criar Ambiente Virtual (Opcional, mas Recomendado)
```

- No Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

- No macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
## Instalar Dependências

- Com o ambiente virtual ativado (se estiver usando), instale as dependências:
```bash
pip install pymupdf Pillow
```

- Caso não use ambiente virtual, apenas pip install pymupdf Pillow será suficiente (contanto que tenha permissões adequadas).

## Estrutura de Diretórios
A estrutura esperada é a seguinte:

```bash
/raiz_do_projeto
├─ processar_pdfs.py
├─ PDF
│   ├─ arquivo1.pdf
│   ├─ arquivo2.pdf
│   └─ ...
└─ Imagens (será criada pelo programa)
```

- Crie uma pasta chamada PDF no diretório raiz (onde está o processar_pdfs.py) e coloque os arquivos PDF que deseja processar dentro dela.
- Ao executar o programa, uma pasta Imagens será criada, contendo subpastas para cada PDF processado. Dentro de cada subpasta, você encontrará as imagens rasterizadas e as imagens extraídas.
## Execução
- No diretório raiz do projeto (onde está o processar_pdfs.py), execute:

```bash
python processar_pdfs.py
```
O programa irá:
- Procurar a pasta PDF no diretório raiz.
- Encontrar todos os arquivos .pdf dentro de PDF.
- Criar a pasta Imagens se ainda não existir.
Para cada PDF:
- Criar uma subpasta em Imagens com o nome do PDF (sem extensão).
- Rasterizar cada página em 300 DPI e salvar como pagina_X_rasterizada.png.
- Extrair cada imagem incorporada do PDF e salvar como pagina_X_imagem_Y.jpg.
- Identificar componentes de imagem individuais (usando get_text("rawdict")) e salvá-los como pagina_X_componente_Z.png.
- Ao final, o programa exibirá mensagens sobre o status do processamento. Para sair, pressione ENTER conforme solicitado.

## Exemplo de Estrutura de Saída
Suponha que você tenha um arquivo MeuPDF.pdf com 2 páginas. A saída será algo como:
```bash
Imagens/
└─ MeuPDF/
   ├─ pagina_1_rasterizada.png
   ├─ pagina_2_rasterizada.png
   ├─ pagina_1_imagem_1.jpg
   ├─ pagina_2_imagem_1.jpg
   ├─ pagina_1_componente_1.png
   └─ pagina_2_componente_1.png
```

## Erros Comuns
"FileNotFoundError":
Verifique se a pasta PDF existe no mesmo diretório que o executável ou o script. Verifique também se há pelo menos um arquivo .pdf dentro dela.

## Problemas com Dependências:
Caso encontre erros de import, verifique se instalou corretamente as dependências (pymupdf e Pillow) e se o ambiente virtual está ativado.
