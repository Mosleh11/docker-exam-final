all:
	docker-compose up -d --build

clean:
	docker-compose down

fclean: clean
	docker system prune -af

# Règle spéciale demandée dans la consigne : nettoie la BDD
purge:
	# Sur Linux 'rm -rf', sur Windows on utilise PowerShell
	# Attention : ceci supprime le dossier data local
	rm -rf data
	# Ou sous Windows si Make fonctionnait : rmdir /s /q data

re: fclean all

.PHONY: all clean fclean re purge