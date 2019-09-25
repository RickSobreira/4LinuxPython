-- update

use 4linux;

select * from pessoa
where id_pessoa = 1;

update pessoa
set nome_pessoa = "Joaquim"
where id_pessoa = 1;

select * from pessoa
where id_pessoa = 1

