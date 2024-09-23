
# GESTOR DE RELATÓRIOS BI

Objetivo desse projeto foi solucionar um problema de custo de licenças para uso não comercial dos relatórios de BI. A empresa solicitante necessitava de um painel administrativo para que seus usuários pudessem ter em um só lugar todos os relatórios de Power BI, com autenticação simples e que pudesse ser feito atualização de acessos e relatórios.

> Problema: O Power BI em sua versão gratuita, gera urls dinâmicas, toda vez que o projeto é atualizado, sendo necessário publicar novamente e compartilhar essa nova url com os usuários do mesmo.
>
> Solução:  Foi criado uma rota /upload onde o admin pode subir uma planilha.xlsx com todos os dados de acessos e relatórios, sem a necessidade de compartilhar links individuais por usuário. Cada usuário acessa a rota /login com seus respectivos acessos e visualizam somente BIs associados ao seu login.



### Tecnologias:

- Python
- Flask
- HTML
- TailwindCSS
- Excel
- Power BI

### Acesso de teste na rota /
login: teste
senha: teste123

### Acesso de teste na rota /upload
login: admin
senha: admin
