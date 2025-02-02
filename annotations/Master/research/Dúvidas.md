# Faz sentido os campos a seguir serem considerados dados pessoais[^1]? É possível identificar uma pessoa a partir desses dados?
	- users
		- created_at
		- updated_at
		- encrypted_password
		- reset_password_token
		- reset_password_sent_at
		- remember_created_at
		- sign_in_count
		- current_sign_in_at
		- last_sign_in_at
		- current_sign_in_ip
		- last_sign_in_ip
		- confirmation_token
		- confirmed_at
		- confirmation_sent_at
		- failed_attempts
		- unlock_token
		- locked_at
		- role_id
		- unconfirmed_email
		- invitation_token
		- invitation_created_at
		- invitation_sent_at
		- invitation_accepted_at
		- invitation_limit
		- invited_by_type
		- invited_by_id
		- invitations_count

Consideramos como indireto.

# Uma vez que precisamos de uma base de dados que represente esta política de privacidade, será necessário criar um vocabulário para represenar esta política de privacidade. Não estaria esta nossa transformação viciada?

Talvez seja uma ameaça à validade da experimentação que estamos fazendo. Todavia, para o modelo ser implementado, esse passo deve ser feito, isto é, adaptar a base de dados ao modelo GDPRov.

# Nosso modelo conecta a politica de retenção ao processo de coleta do dado. Por que optamos por esta abordagem? Por que não conectar diretamente com o dado?


---
[^1]: A definição de dado pessoal é o dado que torna possível identificar uma pessoa natural