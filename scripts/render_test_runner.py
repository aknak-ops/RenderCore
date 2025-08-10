from output_writer import save_render_output
from env_check import get_env_value

def test_render(id, prompt):
    output_dir = get_env_value("OUTPUT_DIR", "output/test")
    content = f"[DRY RUN] Rendered prompt: {prompt}"
    return save_render_output(output_dir, id, content)
