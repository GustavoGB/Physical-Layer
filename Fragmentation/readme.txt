Do arduino Due para o o Uno funciona seamlessly.
Nao sei porque do Uno para o due nao ta indo. Alguma coisa com as portas COM windows?

O controle de fluxo do buffer pra memoria nao tem aqui. No ack nack tem. Nesse espera dois segundos ...
A melhor solucao intermediaria � verificar se o tamanho da mensagem ja � do tamanho do lido no head + 8 bytes

No ack nack o head est� com 3 bytes para o tamanho.
