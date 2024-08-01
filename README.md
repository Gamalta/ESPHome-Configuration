# Configuration ESPHome

- [ESPHome](https://esphome.io/index.html)
- [Installation](https://esphome.io/guides/installing_esphome.html)


## Création de l'environnement virtuel python

```bash
python -m venv .venv 
```

## Lancement de l'environnement

```bash
# linux
sudo su             #via sudo sinon téléversage impossible
source .venv/bin/activate
# windows
.\.venv\Scripts\activate
```

## Commande ESPHome

Validation de configuration
```bash
esphome config ./configuration_file.yaml
```

Compilée la configuration

```bash
esphome compile ./configuration_file.yaml
```

Téléverser la configuration compilée
```bash
esphome upload ./configuration_file.yaml
```

## Ajout dans Home Assistant

```
Paramètres >> Appareils et Services >> ESPHome >> AJOUTER UN APPAREIL
```

- necessite l'adress de l'Hôte ``ex: 192.168.0.[0-50]``
- necessite le port de l'Hôte ``par default: 6053``
- necessite la clé de chiffrement ``[device_name]_api_key dans secrets.yaml``

## Génération d'une API Key

```bash
python api-key-generator.py
```