CREATE DATABASE  IF NOT EXISTS LIVRARIA ; 
USE LIVRARIA;

CREATE 	TABLE  IF NOT  EXISTS AUTOR  ( iD_autor int key primary 
not null  unique , 
nome varchar(40) ,ano_publicacao year  );


s
CREATE TABLE IF NOT exists LIVRO ( ID_LIVRO INT key primary auto_incremet not null  unique  ,
TITULO_LIVRO VARCHAR (25) not null
, preco int not null  ) ;


CREATE TABLE IF NOT EXISTS ITEM_da_venda ( id_venda int key primary   ,
 ID_LIVROS int foreing key , qtd_vendas int   ) ;






CREATE TABLE IF NOT EXISTS venda ( id_venda int  key primary   auto_increment unique   );


CREATE TABLE IF NOT EXISTS

CREATE TABLE IF NOT EXISTS












