# PORTUGUESE VERSION
# 1. Problema de negócio

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core
business é facilitar o encontro e negociações de clientes e restaurantes. Os
restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza
informações como endereço, tipo de culinária servida, se possui reservas, se faz
entregas e também uma nota de avaliação dos serviços e produtos do restaurante,
dentre outras informações.
O CEO Guerra também foi recém contratado e precisa entender melhor o negócio
para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a
Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da
empresa e que sejam gerados dashboards, a partir dessas análises, para responder
às seguintes perguntas:

## Geral

1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

## País

1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4
registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária
distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem
entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam
reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações
registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?

## Cidade

1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de
4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de
2.5?
4. Qual o nome da cidade que possui a maior quantidade de tipos de culinária
distintas?
5. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
reservas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
entregas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que
aceitam pedidos online?

## Restaurantes e tipos de culinária

1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
restaurante com a menor média de avaliação?

# 2. Premissas do negócio

1. As informações do banco de dados foram identificadas conforme abaixo:

| Column | Description |
| --- | --- |
| Restaurant ID | ID do restaurante |
| Restaurant Name | Nome do Restaurante |
| Country Code | Código do País |
| City | Nome da Cidade onde o restaurante está |
| Address | Endereço do restaurante |
| Locality | Localização e pontos de referência do restaurante |
| Locality Verbose | Localização e pontos de referência do restaurante (Mais informações) |
| Longitude | Ponto geográfico de Longitude do Restaurante |
| Latitude | Ponto geográfico de Latitude do Restaurante |
| Cuisines | Tipos de Culinária servidos no restaurante |
| Average Cost for two | Preço Médio de um prato para duas pessoas no restaurante |
| Currency | Moeda do país |
| Has Table booking | Se o restaurante possui serviços de reserva; 1 - Sim; 0 - Não |
| Has Online delivery | Se o restaurante possui serviços de pedido on-line; 1 - Sim; 0 - Não |
| Is delivering now | Se o restaurante faz entregas; 1 - Sim; 0 - Não |
| Switch to order menu | - |
| Price range | Variação de preços do restaurante; 1 a 4 - Quanto maior o valor, mais caro serão os pratos |
| Aggregate rating | Nota média do restaurante |
| Rating color | Código Hexadecimal da cor do restaurante com base em sua nota média |
| Rating text | Categoria em que o restaurante está com base em sua nota média |
| Votes | Quantidade de avaliações que o restaurante já recebeu |
1. Marketplace foi o modelo de negócio assumido.
2. Os 4 principais visões do negócio foram: visão geral, visão por país, visão por cidade e visão por tipos culinários.

# 3. Estratégia da solução

O painel estratégico foi desenvolvido utilizando as métricas que refletem
quatro visões macro do modelo de negócio da empresa, conforme abaixo:

1. Visão Geral:
    1. Quantidade de restaurantes registrados;
    2. Quantidade de países registrados;
    3. Quantidade de cidades registradas;
    4. Quantidade de notas registradas;
    5. Quantidade de tipos culinários registrados;
    6. Mapa com a localização dos restaurantes.
2. Visão por países:
    1. Cidades registradas por país;
    2. Restaurantes registrados por país;
    3. Tipos de culinária registrados por país;
    4. Quantidade de países por tipo culinário;
    5. Quantidade de notas registradas por país;
    6. Média das notas registradas por país.
3. Visão por cidades:
    1. As 10 cidades com mais restaurantes registrados;
    2. Visão de restaurantes no total e que fazem reserva de mesas por cidades e países;
    3. Visão de restaurantes no total e que aceitam pedidos online por cidades e países;
    4. Visão de restaurantes no total e que realizam entrega por cidades e países;
    5. As 10 cidades com média da nota superior a 4, com visão da quantidade de restaurantes;
    6. As 10 cidades com média da nota inferior a 2,5, com visão da quantidade de restaurantes;
    7. As 10 cidades com restaurantes registrados que oferecem mais tipos culinários.
4. Visão por tipos culinários:
    1. Os restaurantes com a melhor média da nota de avaliação, nome da cidade, nome do país e custo médio para refeição de duas pessoas para os seguintes tipos culinários: italiana, americana, japonesa, brasileira e arábica;
    2. Visão das principais informações dos restaurantes ordenados por média de nota e filtros de país e tipo culinário;
    3. Os 10 tipos culinários com melhores notas de avaliação médias;
    4. Os 10 tipos culinários com piores notas de avaliação médias;

# 4. Top 3 Insights de dados

1. A Índia é o país com mais cidades (39%) e restaurantes registrados (52%);
2. Menos da metade dos restaurantes registrados aceitam pedidos online (41%), realizam entrega (20%) e reserva de mesa (7%);
3. O tipo culinário melhor avaliado está definido como “outros”.

# 5. O produto final do projeto

Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.
O painel pode ser acessado através desse link: https://jaquelinepfreitas-zomato-ftc.streamlit.app/

# 6. Conclusão

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam as métricas do negócio da melhor forma possível para o CEO.

# 7. Próximo passos

1. Converter o custo da refeição para duas pessoas para uma moeda única e fazer comparações;
2. Associar a proporção de restaurantes que aceitam pedido online e realizam entrega e/ou reserva de mesas ao tipo culinário, ao custo da refeição e a nota de avaliação.


# ENGLISH VERSION
# 1. Business Problem

Fome Zero is a restaurant marketplace company. In other words, its core business is to facilitate the connection and negotiations between customers and restaurants. Restaurants register within Fome Zero's platform, which provides information such as address, type of cuisine served, availability of reservations, delivery options, and also a rating score for the restaurant's services and products, among other details.
The newly hired CEO, Guerra, needs to gain a better understanding of the business in order to make informed strategic decisions and further boost Fome Zero. To achieve that, he requires a data analysis to be conducted and dashboards to be generated based on these analyses, in order to answer the following questions:

## Overall

1. How many unique registered restaurants are there?
2. How many unique registered countries are there?
3. How many unique registered cities are there?
4. What is the total number of reviews?
5. What is the total number of registered cuisine types?

## By Country

1. Which country has the highest number of registered cities?
2. Which country has the highest number of registered restaurants?
3. Which country has the highest number of restaurants with a price level of 4?
4. Which country has the highest number of distinct cuisine types?
5. Which country has the highest number of reviews?
6. Which country has the highest number of restaurants offering delivery?
7. Which country has the highest number of restaurants accepting reservations?
8. Which country has the highest average number of reviews registered?
9. Which country has the highest average rating score registered?
10. Which country has the lowest average rating score registered?

## By City

1. Which city has the highest number of registered restaurants?
2. Which city has the highest number of restaurants with an average rating above 4?
3. Which city has the highest number of restaurants with an average rating below 2.5?
4. Which city has the highest number of distinct cuisine types?
5. Which city has the highest number of restaurants offering reservations?
6. Which city has the highest number of restaurants offering delivery?
7. Which city has the highest number of restaurants accepting online orders?

## Restaurants and Cuisine Types

1. Which restaurant has the highest number of reviews?
2. Which restaurant has the highest average rating score?
3. Among the restaurants serving Italian cuisine, which one has the highest average rating score?
4. Among the restaurants serving Italian cuisine, which one has the lowest average rating score?
5. Among the restaurants serving American cuisine, which one has the highest average rating score?
6. Among the restaurants serving American cuisine, which one has the lowest average rating score?
7. Among the restaurants serving Arabic cuisine, which one has the highest average rating score?
8. Among the restaurants serving Arabic cuisine, which one has the lowest average rating score?
9. Among the restaurants serving Japanese cuisine, which one has the highest average rating score?
10. Among the restaurants serving Japanese cuisine, which one has the lowest average rating score?

# 2. Business Assumptions

1. The database information was identified as follows:

| Column | Description |
| --- | --- |
| Restaurant ID | Restaurant ID |
| Restaurant Name | Restaurant Name |
| Country Code | Country Code |
| City | City where the restaurant is located |
| Address | Restaurant address |
| Locality | Restaurant's locality and landmarks |
| Locality Verbose | Restaurant's locality and landmarks (additional information) |
| Longitude | Restaurant's longitude geographic point |
| Latitude | Restaurant's latitude geographic point |
| Cuisines | Cuisines served at the restaurant |
| Average Cost for two | Average cost for a meal for two people at the restaurant |
| Currency | Country's currency |
| Has Table booking | Whether the restaurant accepts table reservations; 1 - Yes; 0 - No |
| Has Online delivery | Whether the restaurant offers online delivery services; 1 - Yes; 0 - No |
| Is delivering now | Whether the restaurant is currently delivering; 1 - Yes; 0 - No |
| Switch to order menu | - |
| Price range | Restaurant's price range; 1 to 4 - The higher the value, the more expensive the dishes |
| Aggregate rating | Restaurant's average rating score |
| Rating color | Hexadecimal code representing the restaurant's color based on its average rating score |
| Rating text | Category in which the restaurant falls based on its average rating score |
| Votes | Number of reviews the restaurant has received |

2. The assumed business model is a marketplace.
3. The four main business perspectives considered are: overall view, view by country, view by city, and view by cuisine types.

# 3. Solution Strategy

The strategic dashboard was developed using metrics that reflect four macro perspectives of the company's business model, as follows:

1. Overall View:
    1. Number of registered restaurants;
    2. Number of registered countries;
    3. Number of registered cities;
    4. Number of registered ratings;
    5. Number of registered cuisine types;
    6. Map displaying restaurant locations.
2. View by Country:
    1. Registered cities per country;
    2. Registered restaurants per country;
    3. Registered cuisine types per country;
    4. Number of countries per cuisine type;
    5. Number of registered ratings per country;
    6. Average ratings per country.
3. View by City:
    1. Top 10 cities with the highest number of registered restaurants;
    2. View of restaurants, total and with table booking, by cities and countries;
    3. View of restaurants, total and with online delivery, by cities and countries;
    4. View of restaurants, total and with delivery, by cities and countries;
    5. Top 10 cities with an average rating above 4, displaying the number of restaurants;
    6. Top 10 cities with an average rating below 2.5, displaying the number of restaurants;
    7. Top 10 cities with the highest number of registered restaurants offering the most cuisine types.
4. View by Cuisine Types:
    1. Restaurants with the highest average rating, city name, country name, and average cost for a meal for two people, for the following cuisine types: Italian, American, Japanese, Brazilian, and Arabic;
    2. View of key restaurant information sorted by average rating, with filters for country and cuisine type;
    3. Top 10 cuisine types with the highest average rating scores;
    4. Top 10 cuisine types with the lowest average rating scores.

# 4. Top 3 Data Insights

1. India is the country with the highest number of registered cities (39%) and restaurants (52%);
2. Less than half of the registered restaurants accept online orders (41%), offer delivery (20%), and table reservations (7%);
3. The cuisine type with the highest rating score is categorized as "others".

# 5. Project's Final Product

An online dashboard hosted on a cloud platform and accessible from any internet-connected device.
The dashboard can be accessed through this link: https://jaquelinepfreitas-zomato-ftc.streamlit.app/

# 6. Conclusion

The aim of this project is to create a set of charts and/or tables that present the business metrics in the best possible way for the CEO.

# 7. Next Steps

1. Convert the average cost for a meal for two people to a single currency and make comparisons;
2. Associate the proportion of restaurants that accept online orders, offer delivery, and/or table reservations with cuisine type, average cost for a meal, and rating score.
