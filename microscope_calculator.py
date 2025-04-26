def calculate_real_size(microscope_size, magnification):
    if magnification <= 0:
        raise ValueError("Magnification must be positive.")
    return microscope_size / magnification

# Example usage
microscope_size = float(input("Enter microscope size (μm): "))
magnification = float(input("Enter magnification: "))
real_size = calculate_real_size(microscope_size, magnification)
print(f"Real size: {real_size:.2f} μm")