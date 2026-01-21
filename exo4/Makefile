# Règle standard
all:
	docker-compose up -d --build

# Règle standard
clean:
	docker-compose down

# "purge bdd" : Supprime uniquement les volumes (la base de données)
purge_bdd:
	docker-compose down -v

# "purge all" : Nettoie tout (conteneurs, images, volumes, réseaux) et relance
purge_all:
	docker-compose down -v --rmi all --remove-orphans
	docker system prune -f
	docker-compose up -d --build

.PHONY: all clean purge_bdd purge_all