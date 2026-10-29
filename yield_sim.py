# Commercial West African Batch Cooking Yield & Multi-Channel Financial Twin
# Production Model: Commercial Jollof Rice Batch with Direct Gas COGS & QC Controls

def run_advanced_jollof_twin():
    # 1. Raw Ingredients Cost (GBP)
    raw_ingredients_cost = 4.70 + 12.00 + 2.00 + 0.67 + 1.30 + 3.00 + 2.00 + 3.00  # £28.67
    
    # 2. Direct Fuel Cost (15kg LPG Gas Cylinder @ £56.00 / 30-day lifecycle)
    gas_cost_per_batch = 56.00 / 30.0  # £1.87 per batch
    total_batch_production_cost = raw_ingredients_cost + gas_cost_per_batch  # £30.54
    
    # 3. Yield & Portioning (Blast Chilled Post-Cook Yield Retention)
    usable_cooked_kg = 9.45  # Net yield post thermal reduction & bottom-crust extraction
    portion_weight_kg = 0.45  # 450g serving in 650ml Satco container
    total_portions = usable_cooked_kg / portion_weight_kg  # 21 portions
    
    # 4. Direct Packaging Costs (GBP per unit)
    satco_container = 38.00 / 250  # £0.152
    foil_wrap = 9.00 / 225         # £0.040
    carrier_bag = 26.00 / 250      # £0.104
    total_packaging_cost = satco_container + foil_wrap + carrier_bag  # £0.296
    
    # 5. Unit Level Direct COGS
    food_fuel_cogs_per_kg = total_batch_production_cost / usable_cooked_kg  # £3.23 / kg
    portion_food_fuel_cogs = food_fuel_cogs_per_kg * portion_weight_kg       # £1.45
    total_direct_cogs = portion_food_fuel_cogs + total_packaging_cost      # £1.75 per portion
    
    in_house_price = 7.00
    target_net_profit = in_house_price - total_direct_cogs  # £5.25 (75.0% Gross Margin)
    
    # 6. Delivery Channels (Nominal Comm + 20% VAT + 0.5% Video Audit Dispute Buffer)
    dispute_leakage = 0.005  # Reduced from 3% due to camera-audited packing
    channels = {
        "Just Eat (Full Service)": 0.30,
        "Uber Eats (Full Service)": 0.33,
        "Deliveroo (Full Service)": 0.35,
        "Marketplace Self-Delivery": 0.16,
    }
    
    print("=== ADVANCED JOLLOF RICE OPERATIONAL TWIN ===")
    print(f"Batch Production Cost: £{total_batch_production_cost:.2f} (Food: £{raw_ingredients_cost:.2f} | LPG Gas: £{gas_cost_per_batch:.2f})")
    print(f"Total Direct COGS per Portion: £{total_direct_cogs:.2f}")
    print(f"In-House Base Contribution (£7.00 retail): £{target_net_profit:.2f} (75.0% Gross Margin)\n")
    
    for channel, comm_rate in channels.items():
        effective_comm = (comm_rate * 1.20) + dispute_leakage
        calibrated_price = (target_net_profit + total_direct_cogs) / (1 - effective_comm)
        print(f"{channel}: Effective Fee = {effective_comm*100:.1f}% | Calibrated Retail Price = £{calibrated_price:.2f}")
    
    # Foodhub Model
    foodhub_fee = (in_house_price * 0.034) + 0.20 + (in_house_price * dispute_leakage)
    foodhub_profit = in_house_price - foodhub_fee - total_direct_cogs
    print(f"\nFoodhub (0% Comm, 3.4%+20p Fee + Audit Buffer): Net Profit = £{foodhub_profit:.2f} (68.7% Margin)")

if __name__ == "__main__":
    run_advanced_jollof_twin()
