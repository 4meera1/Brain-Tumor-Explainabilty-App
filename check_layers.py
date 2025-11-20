from tensorflow.keras.models import load_model

model = load_model("final_mobilenet_brain_tumor.keras")

print("\n=== MODEL SUMMARY ===\n")
model.summary()

print("\n=== LAYER NAMES ===\n")
for layer in model.layers:
    print(layer.name, " - ", layer.__class__.__name__)
