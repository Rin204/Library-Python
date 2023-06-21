python3 expansion_all.py

echo "finish copy"

black expansion
ruff --fix expansion
echo "finish format"
