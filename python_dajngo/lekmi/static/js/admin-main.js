// -------------------------- dashboard js
let list = document.querySelectorAll(".navigation li");

function activeLink() {
    list.forEach(item => {
        item.classList.remove("hovered")
    })
    this.classList.add("hovered");

}
// list.forEach((item) => item.addEventListener("mouseover",activeLink));
list.forEach((item) => item.addEventListener("click", activeLink));


// -------- sidebar toggle js

let sdtoggle = document.querySelector(".sidebarToggle");
let navigation = document.querySelector(".navigation");
let dbmain = document.querySelector(".dashboard-main");

sdtoggle.onclick = function () {
    navigation.classList.toggle("active");
    dbmain.classList.toggle("active");
}


// ------------- add product page js


let newColorIndex = 0;
let newIngredientIndex = 0;

document.addEventListener("DOMContentLoaded", () => {
    // Add Color Button
    const addColorBtn = document.getElementById("addColorBtn");
    const addIngredientBtn = document.getElementById("addIngredientBtn");

    if (addColorBtn) {
        addColorBtn.addEventListener("click", addColorBlock);
    }

    if (addIngredientBtn) {
        addIngredientBtn.addEventListener("click", addIngredientBlock);
    }

    // Add/Remove uploads for existing colors
    const colorCheckboxes = document.querySelectorAll(".existing-color-checkbox");
    const existingColorUploadsSection = document.getElementById("existingColorUploads");

    colorCheckboxes.forEach((checkbox) => {
        checkbox.addEventListener("change", function () {
            const colorName = this.value;
            const uploadFieldId = `upload-${colorName.toLowerCase()}`;

            if (this.checked) {
                const uploadBlock = document.createElement("div");
                uploadBlock.classList.add("mb-2");
                uploadBlock.id = uploadFieldId;
                uploadBlock.innerHTML = `
          <label class="form-label">Images for <strong>${colorName}</strong></label>
          <input type="file" name="existing_color_images[${colorName}][]" class="form-control" multiple required>
        `;
                existingColorUploadsSection.appendChild(uploadBlock);
            } else {
                const toRemove = document.getElementById(uploadFieldId);
                if (toRemove) toRemove.remove();
            }
        });
    });

    // Event delegation for removing blocks (color/ingredient)
    document.addEventListener("click", function (e) {
        if (e.target.classList.contains("remove-block-btn")) {
            const block = e.target.closest(".color-block, .ingredient-block");
            if (block) block.remove();
        }
    });
});

// Function: Add New Color Block
function addColorBlock() {
    newColorIndex++;
    const newColorSection = document.getElementById('colorContainer');

    const colorBlock = document.createElement('div');
    colorBlock.classList.add('color-block');
    colorBlock.innerHTML = `
    <div class="row mb-2">
      <div class="col-md-4">
        <label class="form-label">Color Name</label>
        <input type="text" name="new_colors[${newColorIndex}][name]" class="form-control" required>
      </div>
      <div class="col-md-3">
        <label class="form-label">Color Picker</label>
        <input type="color" name="new_colors[${newColorIndex}][code]" class="form-control form-control-color" value="#ffffff">
      </div>
      <div class="col-md-4">
        <label class="form-label">Upload Images</label>
        <input type="file" name="new_colors[${newColorIndex}][images][]" class="form-control" multiple required>
      </div>
      <div class="col-md-1 position-relative">
        <button type="button" class="btn btn-outline-danger btn-sm remove-block-btn position-absolute top-50">✖</button>
      </div>
    </div>
  `;
    newColorSection.appendChild(colorBlock);
}

// Function: Add New Ingredient Block
function addIngredientBlock() {
    newIngredientIndex++;
    const ingredientSection = document.getElementById('ingredientContainer');

    const ingredientBlock = document.createElement('div');
    ingredientBlock.classList.add('ingredient-block', 'mb-2');
    ingredientBlock.innerHTML = `
    <div class="input-group">
      <input type="text" name="new_ingredients[]" class="form-control" placeholder="New Ingredient Name" required>
      <button type="button" class="btn btn-outline-danger remove-block-btn">✖</button>
    </div>
  `;
    ingredientSection.appendChild(ingredientBlock);
}


// -------------search logic for enter

document.addEventListener("DOMContentLoaded", () => {
  const searchInput = document.getElementById("adminSearchInput");

  if (searchInput) {
    searchInput.addEventListener("keydown", (event) => {
      if (event.key === "Enter") {
        event.preventDefault();  // Prevent default form submission or page reload
        const query = searchInput.value.trim();
        if (query) {
          console.log("Enter pressed, search query:", query);
          // You can handle sending this query to backend here
        }
      }
    });
  }
});
