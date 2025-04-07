# File to check
file="/home/arm/Codes/exam/scripting exam/shell/file.txt"

# Function to calculate hash
calculate_hash() {
    sha256sum "$file" | awk '{print $1}'
}

# Check if file exists
if [ ! -f "$file" ]; then
    echo "File '$file' does not exist."
    exit 1
fi

# Calculate and display original hash
original_hash=$(calculate_hash)
echo "Original hash: $original_hash"

# Wait for changes
read -p "Make changes to the file and press Enter when done..."

# Recalculate and display new hash
new_hash=$(calculate_hash)
echo "New hash: $new_hash"

# Compare hashes
if [ "$original_hash" == "$new_hash" ]; then
    echo "✅ File integrity is intact."
else
    echo "⚠️ File has been modified."
fi
