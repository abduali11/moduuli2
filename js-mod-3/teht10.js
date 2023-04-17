const form = document.querySelector('#source');

form.addEventListener('submit', (event) => {
  event.preventDefault(); // prevent form submission

  const firstName = document.querySelector('input[name="firstname"]').value;
  const lastName = document.querySelector('input[name="lastname"]').value;
  const output = `Your name is ${firstName} ${lastName}`;

  const target = document.querySelector('#target');
  target.textContent = output;
});
