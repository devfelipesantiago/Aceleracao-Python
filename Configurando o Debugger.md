# Configurando o Debugger

Depois de tudo o que você viu de testes em Python até aqui, desde o básico até geração de dados falsos com `faker`, os testes começam a ficar mais complexos e, por isso, as ferramentas de depuração se tornam indispensáveis.

Como você já viu, o _debugger_ do VS Code já se integra muito bem com o _test runner_ do Python usando o _Pytest_. Mas, em cenários mais complexos, a configuração do _debugger_ pode não ser suficiente. Alguns exemplos são:

- Quando o código recebe parâmetros de entrada que não são conhecidos.
- Quando o código depende de variáveis de ambiente específicas.
- Quando o bug ocorre dentro do código de uma biblioteca externa.
- Quando o bug ocorre em um código que é executado em um _container_.

## Acessando as configurações do _debugger_

As configurações de execução do _debugger_ podem ser ajustadas no arquivo `launch.json`, na pasta `.vscode` de seu projeto. Uma forma fácil de criar esse arquivo é:

1. Abrir o menu de _debug_ do VS Code (atalho `Ctrl+Shift+D` ou `Cmd+Shift+D` no Mac).
2. Clicar em “create a launch.json file” (ou “crie um arquivo launch.json”, no VS Code em português).
3. Escolher a opção “Python”.
4. Escolher uma das opções de configuração disponíveis.

Isso vai criar um arquivo `launch.json` com uma configuração básica para executar o arquivo atualmente aberto no editor. A partir daí, você pode ajustar as configurações de acordo com a sua necessidade e, inclusive, adicionar novas configurações!

|![Criação do arquivo `launch.json` com configurações Python](https://content-assets.betrybe.com/prod/b5abb80e-cd69-4187-827b-5bafa7d9bd5e-Cria%C3%A7%C3%A3o%20do%20arquivo%20%60launch.json%60%20com%20configura%C3%A7%C3%B5es%20Python.gif)|
|---|
|Criação do arquivo `launch.json` com configurações Python|

Você também pode criar esse arquivo manualmente.

## Ajustando parâmetros de execução do _debugger_

O primeiro ajuste que deve ser feito ao criar uma configuração customizada de _debug_ é o nome da configuração. Isso é importante porque quando há múltiplas configurações ativas podemos nos confundir com os parâmetros de cada uma.

Para isso, ajuste o valor da propriedade `name` para algo que faça sentido para você. No exemplo a seguir, utilize o nome `"Python: exemplo Trybe"`.

### Habilitando o reset automático do _debugger_

Por padrão, o _debugger_ do VS Code não reinicia sua execução quando o arquivo é alterado. Porém, isso pode ser muito útil quando se está desenvolvendo, pois evita ter que reiniciar o _debugger_ manualmente a cada alteração.

Para habilitar essa funcionalidade, basta adicionar a seguinte configuração:

```diff
    {
        "name": "Python: exemplo Trybe",
        ...
+       "autoReload": {
+           "enable": true
+       }
    }
```

Com essa configuração, você pode, por exemplo, criar uma nova variável em seu código e, ao executar o comando de _Step Over_ (`F10`), o _debugger_ vai reiniciar a execução do código e a nova variável vai estar disponível. Isso é muito útil para testar novas funcionalidades sem ter de reiniciar o _debugger_ e repetir todos os passos a cada alteração.

### Habilitando o debug de bibliotecas externas

Por padrão, o _debugger_ do VS Code não executa o código de bibliotecas externas. Isso é feito para evitar que o _debugger_ entre em um código que não é de sua responsabilidade e, assim, dificulte a depuração do código que está em desenvolvimento.

Mas, em alguns casos, é preciso depurar o código de uma biblioteca externa. Para isso, é necessário ajustar a opção `justMyCode` e definir o valor como `false`.

```diff
    {
        "name": "Python: exemplo Trybe",
        ...
-       "justMyCode": true
+       "justMyCode": false
    }
```

Com essa configuração, o comando de Step Into (`F11`) vai entrar no código de bibliotecas externas.

### Definindo valores de variáveis de ambiente

Em alguns casos, o código que está sendo depurando depende de variáveis de ambiente específicas. Por exemplo, se o código depende de uma variável de ambiente `DATABASE_URL`, é necessário definir essa variável antes de executar o código.

Para isso, pode-se definir a propriedade `env` na configuração do _debugger_:

```diff
    {
        "name": "Python: exemplo Trybe",
        ...
+       "env": {
+           "DEBUG_MODE": "true"
+       }
    }
```

### Configurando o _debugger_ do testador do VS Code

O testador do VS Code, como já foi visto, dá a possibilidade de executar os testes em modo _debug_. Por baixo dos panos, o VS Code utiliza uma configuração de debug específica para isso e, por isso, é preciso ajustar essa configuração separadamente.

Para isso, basta adicionar uma configuração com o campo `"purpose"` definido como `["debug-tests"]`:

```json
{
    // outras configurações
    {
        "name": "Python: debugando meus testes", 
        "type": "python",
        "request": "launch",
        "purpose": [
            "debug-test"
        ],
        "console": "integratedTerminal",
        "justMyCode": false,
    },
    // outras configurações
}
```