-- SELECT

use 4linux;

select * from pessoa;

select * from pessoa
where nac_pessoa = "Brasileira";

select * from pessoa
where idade_pessoa > 18;

select * from pessoa
where nome_pessoa like "Ric%";

