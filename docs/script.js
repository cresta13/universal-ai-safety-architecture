const modeButtons = document.querySelectorAll('.mode');
const panels = document.querySelectorAll('.panel');

modeButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const mode = button.dataset.mode;
    modeButtons.forEach((item) => item.classList.toggle('active', item === button));
    panels.forEach((panel) => panel.classList.toggle('active', panel.dataset.panel === mode));
  });
});
