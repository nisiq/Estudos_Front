Class
    permite ao CSS selecionar e acessar elementos específicos através dos seletores de classe.
    Para estilizar uma classe no CSS é necessário utilizar o ponto final antes de chamar o nome atribuído à classe
    https://developer.mozilla.org/pt-BR/docs/Web/HTML/Global_attributes/class
    https://www.alura.com.br/artigos/nomes-de-classes-no-css



Reset CSS
    Cada navegador tem a sua apresentação por padrão e esse comportamento individualizado pode gerar conflitos de layout diante do seu projeto web

    * {
    margin: 0;
    padding: 0;
    }

    Para resetar os padrões dos navegadores de forma simples utilizamos propriedades margin,
    que define a área de margem nos quatro lados do elemento (cima, direita, baixo, esquerda),
    e padding, que define a área de preenchimento interna nos mesmos quatro lados do elemento, 
    ambas com valor igual à 0.



CSS Box Model
    Content - O conteúdo da caixa, onde aparecem texto e imagens
    Padding - Limpa uma área ao redor do conteúdo. O enchimento é transparente
    Border - Uma borda que contorna o preenchimento e o conteúdo
    Margin - Limpa uma área fora da borda. A margem é transparente

        Demonstração do modelo de caixa:

        div {
        width: 300px;
        border: 15px solid green;
        padding: 50px;
        margin: 20px;
        }