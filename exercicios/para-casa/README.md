# Exercício de Casa 🏠 


## 👩🏻‍💻 Crie uma classe base chamada Veiculo com os seguintes atributos:

- modelo: o modelo do veículo (uma string).
- ano: o ano de fabricação do veículo (um número inteiro).
preco: o preço do veículo (um número decimal).
Na classe Veiculo, implemente um método chamado `calcular_imposto()` que retorna o imposto a ser pago pelo veículo. O imposto é calculado como 10% do preço do veículo.

Crie uma classe chamada Carro que herda da classe Veiculo. Adicione um atributo adicional:

- marca: a marca do carro (uma string).
Na classe Carro, implemente um método chamado desconto() que retorna um desconto de 5% no preço do carro.

Crie uma classe chamada Moto que também herda da classe Veiculo. Adicione um atributo adicional:

- cilindrada: a cilindrada da moto (um número inteiro).
Na classe Moto, implemente um método chamado `calcular_imposto()` que calcula o imposto a ser pago pela moto. O imposto para motos é de 5% do preço do veículo.

Crie instâncias de Carro e Moto, atribuindo valores adequados aos atributos de cada veículo.

Calcule e imprima o imposto a ser pago por cada veículo usando o método `calcular_imposto()`.



## 🧠 Exercício de Herança em Python: Sistema de Gerenciamento de Funcionários (Exercicío Avançado Extra)

Você está encarregado de criar um sistema de gerenciamento de funcionários para uma empresa. O sistema deve ser capaz de lidar com diferentes tipos de funcionários e calcular seus salários com base em suas características específicas. Para isso, você precisa implementar a hierarquia de classes apropriada usando herança em Python.

Instruções:

Crie uma classe base chamada Funcionario com os seguintes atributos:

 - nome: o nome do funcionário.
 - salario: o salário base do funcionário (inicialmente definido como 0).

A classe Funcionario deve ter um método chamado `calcular_pagamento()` que retorna o pagamento do funcionário. No entanto, este método deve ser definido como um método abstrato (utilizando `pass`) uma vez que cada tipo de funcionário (temporário e integral) calculará o pagamento de maneira diferente.

Crie uma classe chamada FuncionarioTemporario, que herda da classe Funcionario. Esta classe deve ter os seguintes atributos adicionais:

- salario_por_hora: o salário por hora do funcionário temporário.
- horas_trabalhadas: o número de horas trabalhadas pelo funcionário temporário.
Na classe FuncionarioTemporario, implemente o método `calcular_pagamento()` para calcular o pagamento do funcionário temporário com base no salário por hora e nas horas trabalhadas.

Crie uma classe chamada FuncionarioIntegral, que também herda da classe Funcionario. Esta classe deve ter um atributo adicional:

- salario_mensal: o salário mensal do funcionário integral.
Na classe FuncionarioIntegral, implemente o método `calcular_pagamento()` para calcular o pagamento do funcionário integral, que é igual ao seu salário mensal.

Crie instâncias de FuncionarioTemporario e FuncionarioIntegral, atribuindo valores adequados aos atributos de cada funcionário.

Calcule e imprima o pagamento de cada funcionário usando o método `calcular_pagamento()`.

---

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [ ] Fiz o fork do repositório.
- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [ ] Resolvi o exercício.
- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)
- [ ] Criei um Pull Request seguindo as orientaçoes que estao nesse [documento](https://github.com/mflilian/repo-example/blob/main/exercicios/para-casa/instrucoes-pull-request.md).
