import streamlit as st

# ---------------------------------------------------------
# SMART MEAL FINDER - STREAMLIT WEB APP
# Orange-themed recipe suggestions from available ingredients
# ---------------------------------------------------------

RECIPES = [
    {
        "name": "Jollof Rice",
        "ingredients": ["rice", "tomato", "pepper", "onion", "oil", "salt"],
        "instructions": "Blend or chop the tomato and pepper. Fry with onion and oil, add water and rice, season, then cook until tender."
    },
    {
        "name": "Egg and Yam",
        "ingredients": ["yam", "egg", "onion", "oil", "salt"],
        "instructions": "Boil the yam until tender. Beat the eggs with chopped onion and salt, then fry in a little oil."
    },
    {
        "name": "Vegetable Omelette",
        "ingredients": ["egg", "tomato", "onion", "pepper", "oil", "salt"],
        "instructions": "Beat the eggs. Mix in chopped vegetables and salt, then cook gently in a lightly oiled pan."
    },
    {
        "name": "Beans and Plantain",
        "ingredients": ["beans", "plantain", "onion", "oil", "salt"],
        "instructions": "Cook the beans until soft and season to taste. Boil, roast, or pan-cook the plantain until tender."
    },
    {
        "name": "Spaghetti in Tomato Sauce",
        "ingredients": ["spaghetti", "tomato", "onion", "pepper", "oil", "salt"],
        "instructions": "Boil the spaghetti. Cook tomato, onion, and pepper in a little oil, season, and mix with the drained pasta."
    },
    {
        "name": "Pancakes",
        "ingredients": ["flour", "egg", "milk", "sugar", "oil"],
        "instructions": "Mix flour, egg, milk, and a little sugar into a smooth batter. Cook small portions in a lightly oiled pan."
    },
    {
        "name": "Akara",
        "ingredients": ["beans", "onion", "pepper", "oil", "salt"],
        "instructions": "Soak and peel the beans, blend with onion and pepper, add salt, then fry small spoonfuls in hot oil with adult supervision."
    },
    {
        "name": "Simple Sandwich",
        "ingredients": ["bread", "egg", "tomato", "onion"],
        "instructions": "Cook the egg, slice the vegetables, and layer everything between slices of bread."
    },
    {
        "name": "Fried Rice",
        "ingredients": ["rice", "carrot", "peas", "onion", "oil", "salt"],
        "instructions": "Cook the rice and let it cool. Stir-fry chopped vegetables in a little oil, add the rice, and season."
    },
    {
        "name": "Potato Porridge",
        "ingredients": ["potato", "tomato", "onion", "pepper", "oil", "salt"],
        "instructions": "Peel and cut the potatoes. Simmer with chopped tomato, onion, pepper, oil, water, and salt until soft."
    },
    {
        "name": "Tomato Egg Sauce",
        "ingredients": ["egg", "tomato", "onion", "pepper", "oil", "salt"],
        "instructions": "Cook chopped tomato, onion, and pepper in a little oil. Add beaten eggs and stir until cooked through."
    },
    {
        "name": "Vegetable Stir-Fry",
        "ingredients": ["carrot", "cabbage", "onion", "oil", "salt"],
        "instructions": "Slice the vegetables and stir-fry them in a little oil until tender-crisp. Season lightly."
    },
    {
        "name": "Boiled Rice",
        "ingredients": ["rice", "water", "salt"],
        "instructions": "Rinse the rice, add to boiling water with a little salt, and cook until tender. Drain if needed."
    },
    {
        "name": "Garlic-Free Tomato Pasta",
        "ingredients": ["pasta", "tomato", "onion", "oil", "salt"],
        "instructions": "Boil the pasta. Simmer chopped tomato and onion in oil, season, and toss with the pasta."
    },
    {
        "name": "Boiled Plantain",
        "ingredients": ["plantain", "water"],
        "instructions": "Peel the plantain, cut into pieces, and boil until tender."
    },
    {
        "name": "Oatmeal",
        "ingredients": ["oats", "milk", "sugar"],
        "instructions": "Simmer oats with milk or water, stirring until soft. Add a little sugar if desired."
    },
    {
        "name": "Chicken Tomato Stew",
        "ingredients": ["chicken", "tomato", "onion", "pepper", "oil", "salt"],
        "instructions": "Cook chicken thoroughly. Prepare a tomato, onion, and pepper sauce, add the chicken, and simmer until piping hot."
    },
    {
        "name": "Moi Moi",
        "ingredients": ["beans", "pepper", "onion", "oil", "salt"],
        "instructions": "Soak and peel the beans, blend with pepper and onion, add a little oil and salt, then steam in suitable heat-safe containers until fully cooked."
    },
    {
        "name": "Boiled Egg",
        "ingredients": ["egg", "water"],
        "instructions": "Place eggs in water, bring to a boil, and cook until firm. Cool before peeling."
    },
    {
        "name": "Cabbage and Carrot Salad",
        "ingredients": ["cabbage", "carrot"],
        "instructions": "Wash the vegetables well, finely slice the cabbage, grate the carrot, and mix together."
    },
    {
        "name": "Yam Porridge",
        "ingredients": ["yam", "tomato", "onion", "pepper", "oil", "salt"],
        "instructions": "Cut yam into cubes. Simmer with tomato, onion, pepper, oil, water, and salt until soft."
    },
    {
        "name": "Egg Fried Rice",
        "ingredients": ["rice", "egg", "carrot", "onion", "oil", "salt"],
        "instructions": "Cook and cool the rice. Scramble the egg, stir-fry onion and carrot, then add the rice and combine."
    },
]


ALIASES = {
    "eggs": "egg",
    "tomatoes": "tomato",
    "onions": "onion",
    "peppers": "pepper",
    "green pepper": "pepper",
    "bell pepper": "pepper",
    "sweet pepper": "pepper",
    "potatoes": "potato",
    "carrots": "carrot",
    "peas": "peas",
    "cabbages": "cabbage",
    "oats": "oats",
    "spag": "spaghetti",
    "noodles": "noodles",
    "groundnut oil": "oil",
    "vegetable oil": "oil",
    "palm oil": "oil",
    "maggi": "seasoning",
    "stock cube": "seasoning",
    "seasoning cube": "seasoning",
}


def normalize_ingredient(ingredient: str) -> str:
    """Clean an ingredient and handle common alternative names."""
    ingredient = ingredient.strip().lower()
    return ALIASES.get(ingredient, ingredient)


def find_meals(raw_text: str):
    """Return recipes ranked by how many extra ingredients they need."""
    user_ingredients = {
        normalize_ingredient(item)
        for item in raw_text.split(",")
        if item.strip()
    }

    matches = []
    for recipe in RECIPES:
        required = set(recipe["ingredients"])
        missing = required - user_ingredients
        matched = required & user_ingredients

        # Show a recipe only when at least one ingredient matches.
        if matched:
            matches.append({
                "recipe": recipe,
                "missing": missing,
                "matched_count": len(matched),
                "missing_count": len(missing),
            })

    matches.sort(key=lambda item: (
        item["missing_count"],
        -item["matched_count"],
        item["recipe"]["name"]
    ))
    return matches


# Page setup
st.set_page_config(
    page_title="Smart Meal Finder",
    page_icon="🍊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Orange theme styling. Streamlit also supports theme settings in .streamlit/config.toml.
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFF3E6;
    }
    [data-testid="stHeader"] {
        background-color: rgba(255, 243, 230, 0.9);
    }
    .hero {
        background: linear-gradient(120deg, #E87516, #F59B42);
        padding: 1.6rem 1.8rem;
        border-radius: 18px;
        color: white;
        margin-bottom: 1rem;
    }
    .hero h1 {
        color: white;
        margin: 0 0 0.35rem 0;
        font-size: 2.25rem;
    }
    .hero p {
        color: white;
        margin: 0;
        font-size: 1.05rem;
    }
    .meal-card {
        background: #FFFFFF;
        border: 1px solid #F2B27E;
        border-left: 6px solid #E87516;
        border-radius: 12px;
        padding: 1rem 1.1rem;
        margin: 0.6rem 0 0.9rem 0;
    }
    .meal-card h3 {
        color: #713400;
        margin: 0 0 0.4rem 0;
    }
    .ready-label {
        color: #287A3D;
        font-weight: 700;
    }
    .missing-label {
        color: #A64B00;
        font-weight: 700;
    }
    div.stButton > button[kind="primary"] {
        background-color: #E87516;
        border-color: #E87516;
        color: white;
    }
    div.stButton > button[kind="primary"]:hover {
        background-color: #A64B00;
        border-color: #A64B00;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown(
    """
    <div class="hero">
        <h1>🍊 Smart Meal Finder</h1>
        <p>Turn the ingredients you have into delicious meal ideas.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar: instructions and examples
with st.sidebar:
    st.header("🥕 How to use")
    st.write("1. Enter the ingredients you have.")
    st.write("2. Separate each ingredient with a comma.")
    st.write("3. Click **Find My Meals**.")
    st.write("4. Check which meals you can make now and what else you may need.")
    st.divider()
    st.subheader("Try an example")
    if st.button("Use: rice, egg, tomato, onion", use_container_width=True):
        st.session_state["ingredients_input"] = "rice, egg, tomato, onion"
        st.session_state["run_search"] = True
    if st.button("Use: yam, egg, oil, salt", use_container_width=True):
        st.session_state["ingredients_input"] = "yam, egg, oil, salt"
        st.session_state["run_search"] = True
    st.caption("This version uses a built-in recipe database and works without an AI API key.")

st.subheader("What ingredients do you have?")
st.caption("Enter ingredients separated by commas. Example: rice, egg, tomato, onion")

if "ingredients_input" not in st.session_state:
    st.session_state["ingredients_input"] = ""
if "run_search" not in st.session_state:
    st.session_state["run_search"] = False

def clear_inputs():
    """Reset the input and search state before the app reruns."""
    st.session_state["ingredients_input"] = ""
    st.session_state["run_search"] = False


with st.form("ingredient_form", clear_on_submit=False):
    raw_text = st.text_input(
        "Available ingredients",
        key="ingredients_input",
        placeholder="e.g. rice, egg, tomato, onion",
        label_visibility="collapsed",
    )
    col1, col2 = st.columns([1, 1])
    with col1:
        search_clicked = st.form_submit_button("🍽️ Find My Meals", type="primary", use_container_width=True)
    with col2:
        clear_clicked = st.form_submit_button("Clear", on_click=clear_inputs, use_container_width=True)

if search_clicked or st.session_state.get("run_search", False):
    st.session_state["run_search"] = False
    if not raw_text.strip():
        st.warning("Please enter at least one ingredient, separated by commas.")
    else:
        matches = find_meals(raw_text)
        if not matches:
            st.info(
                "No matching meals found yet. Try common ingredients such as rice, egg, "
                "tomato, yam, beans, plantain, or potato."
            )
        else:
            ready_meals = [item for item in matches if not item["missing"]]
            st.markdown("### Your meal suggestions")
            st.write(
                f"Found **{len(matches)}** meal idea(s), including "
                f"**{len(ready_meals)}** that match all listed recipe ingredients."
            )

            if ready_meals:
                st.success("Meals you can make with the ingredients listed")
                for item in ready_meals:
                    recipe = item["recipe"]
                    with st.container(border=True):
                        st.markdown(f"#### 🍽️ {recipe['name']}")
                        st.markdown('<span class="ready-label">READY TO MAKE</span>', unsafe_allow_html=True)
                        st.write("**Recipe ingredients:** " + ", ".join(recipe["ingredients"]))
                        st.write("**How to make it:** " + recipe["instructions"])

            other_meals = [item for item in matches if item["missing"]]
            if other_meals:
                st.markdown("### Other ideas (you may need extra ingredients)")
                for item in other_meals:
                    recipe = item["recipe"]
                    missing = sorted(item["missing"])
                    with st.container(border=True):
                        st.markdown(f"#### 🍽️ {recipe['name']}")
                        st.markdown(
                            f'<span class="missing-label">Still needed: {", ".join(missing)}</span>',
                            unsafe_allow_html=True,
                        )
                        st.write("**Recipe ingredients:** " + ", ".join(recipe["ingredients"]))
                        st.write("**How to make it:** " + recipe["instructions"])

st.divider()
st.caption("Smart Meal Finder • Beginner-friendly Python project • Recipe matches are based on the built-in database.")
