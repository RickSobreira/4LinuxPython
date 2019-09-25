-- delete

use 4linux;

select * from pessoa;

delete from pessoa
where nac_pessoa = "Brasileira";

select * from pessoa;


