# Règle par défaut : lance tout avec docker-compose
all:
	docker-compose up -d --build

# Arrête et supprime les conteneurs
clean:
	docker-compose down

# Supprime conteneurs, réseaux ET les images (nettoyage complet)
fclean: clean
	docker system prune -af

# On nettoie tout et on relance
re: fclean all

.PHONY: all clean fclean re