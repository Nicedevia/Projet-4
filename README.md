# Projet-4
read me
Mehdi ok
Briac ok*

 python -m venv .venv                                                                                                         
 .venv\Scripts\Activate.ps1    


Exécuter les tests
Pour exécuter les tests avec pytest, ouvrez un terminal et tapez :
pytest

Exécution de tests spécifiques
pytest name.py::namefonction_test 

Générer des rapports
pytest --junitxml=report.xml

rapport plus detaillé
pip install pytest-html
pytest --html=report.html

Debugging et Tracing
Pour activer le mode de traçage qui permet de voir les appels de fonctions :
pytest -v --tb=short