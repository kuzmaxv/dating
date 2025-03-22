// Сохранение профиля
document.getElementById('create-profile-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('user_id', 123); // Замените на реальный ID пользователя
    formData.append('city', document.getElementById('city').value);
    formData.append('age', document.getElementById('age').value);
    formData.append('gender', document.getElementById('gender').value);
    formData.append('height', document.getElementById('height').value);
    formData.append('eye_color', document.getElementById('eye-color').value);
    formData.append('hair_color', document.getElementById('hair-color').value);
    formData.append('bio', document.getElementById('bio').value);
    formData.append('interests', document.getElementById('interests').value);
    formData.append('hobbies', document.getElementById('hobbies').value);
    formData.append('goals', document.getElementById('goals').value);

    const photos = document.getElementById('photos').files;
    for (let i = 0; i < photos.length; i++) {
        formData.append('photos', photos[i]);
    }

    const response = await fetch('/api/save_profile', {
        method: 'POST',
        body: formData,
    });

    if (response.ok) {
        alert('Профиль успешно сохранен!');
    } else {
        alert('Ошибка при сохранении профиля.');
    }
});

// Поиск анкет
document.getElementById('search-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const searchData = {
        city: document.getElementById('search-city').value,
        age_min: document.getElementById('search-age-min').value,
        age_max: document.getElementById('search-age-max').value,
        gender: document.getElementById('search-gender').value,
        height_min: document.getElementById('search-height-min').value,
        height_max: document.getElementById('search-height-max').value,
        eye_color: document.getElementById('search-eye-color').value,
        hair_color: document.getElementById('search-hair-color').value,
        interests: document.getElementById('search-interests').value,
    };

    const response = await fetch('/api/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(searchData),
    });

    const profiles = await response.json();
    displayProfiles(profiles);
});

// Отображение результатов поиска
function displayProfiles(profiles) {
    const profilesList = document.getElementById('profiles-list');
    profilesList.innerHTML = '';

    profiles.forEach(profile => {
        const profileCard = document.createElement('div');
        profileCard.className = 'profile-card';

        profileCard.innerHTML = `
            <img src="${profile.photo_urls[0]}" alt="Фото">
            <h3>${profile.name}</h3>
            <p>${profile.age} лет, ${profile.city}</p>
            <p>${profile.bio}</p>
        `;

        profilesList.appendChild(profileCard);
    });
}