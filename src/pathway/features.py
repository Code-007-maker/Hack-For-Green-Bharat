import pathway as pw

def compute_environmental_metrics(stream):
    """
    Performs streaming feature engineering on the mask data.
    """
    
    # 1. Vegetation Index (Health of ecosystem)
    # Ratio of live green vegetation (Trees/Bushes) to total landscape
    stream = stream.select(
        *pw.this,
        vegetation_index = pw.this.vegetation_pixels / pw.this.total_pixels
    )
    
    # 2. Drought Risk Score
    # High dry grass and high ground exposure increases risk
    stream = stream.select(
        *pw.this,
        drought_risk = (pw.this.dry_grass_pixels + (0.5 * pw.this.ground_pixels)) / pw.this.total_pixels
    )
    
    # 3. Rock Density (Terrain complexity)
    stream = stream.select(
        *pw.this,
        rock_density = pw.this.rock_pixels / pw.this.total_pixels
    )
    
    # 4. Binary Alerts
    stream = stream.select(
        *pw.this,
        eco_alert = pw.if_else(pw.this.drought_risk > 0.6, "HIGH_RISK_DROUGHT", "STABLE")
    )
    
    return stream

def create_rag_document(row):
    """
    Converts streaming metrics into natural language descriptions for the RAG index.
    """
    return f"At {row['timestamp']}, location ({row['location_lat']:.4f}, {row['location_lon']:.4f}) " \
           f"monitored. Vegetation Index: {row['vegetation_index']:.2%}, " \
           f"Drought Risk: {row['drought_risk']:.2%}, Status: {row['eco_alert']}. " \
           f"Rock density is {row['rock_density']:.2%}."
