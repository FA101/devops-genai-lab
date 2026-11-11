"""OrderService (versão simplificada) - cálculo de frete e total do pedido.

Projeto Integrador - Unidade 5 (DevOps + GenAI).
Na branch feature/nova-logica você vai introduzir um bug intencional
neste arquivo (veja o passo a passo).
"""
import os

# Taxa administrativa lida da configuração (variável de ambiente).
# Atenção: variáveis de ambiente SEMPRE chegam como texto (str).
ADMIN_FEE = float(os.getenv("ADMIN_FEE", "5.0"))

PRICE_PER_KG = 1.5
PRICE_PER_KM = 0.1


def calculate_shipping(weight_kg: float, distance_km: float) -> float:
    """Calcula o frete: peso + distância + taxa administrativa."""
    base_price = weight_kg * PRICE_PER_KG + distance_km * PRICE_PER_KM
    return round(base_price + ADMIN_FEE, 2)


def calculate_order_total(items_total: float, weight_kg: float, distance_km: float) -> float:
    """Total do pedido = soma dos itens + frete."""
    return round(items_total + calculate_shipping(weight_kg, distance_km), 2)


if __name__ == "__main__":
    print("Frete:", calculate_shipping(10, 100))
    print("Total:", calculate_order_total(200, 10, 100))
