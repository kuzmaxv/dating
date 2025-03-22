// Показ индикатора загрузки
function showLoading() {
    document.getElementById('loading').style.display = 'block';
}

// Скрытие индикатора загрузки
function hideLoading() {
    document.getElementById('loading').style.display = 'none';
}

// Валидация данных формы
function validateForm(data) {
    if (data.age < 18 || data.age > 100) {
        alert('Возраст должен быть от 18 до 100 лет.');
        return false;
    }
    if (data.height < 100 || data.height > 250) {
        alert('Рост должен быть от 100 до 250 см.');
        return false;
    }
    return true;
}

// Сохранение профиля
document.getElementById('create-profile-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    showLoading();

    const formData = new FormData();
    formData.append('user_id', 123); // Замените на реальный ID пользователя
    formData.append('city', document.getElementById('city').value);
    formData.append('age', parseInt(document.getElementById('age').value));
    formData.append('gender', document.getElementById('gender').value);
    formData.append('height', parseInt(document.getElementById('height').value));
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

    // Валидация данных
    const formDataObj = Object.fromEntries(formData.entries());
    if (!validateForm(formDataObj)) {
        hideLoading();
        return;
    }

    try {
        const response = await fetch('/api/save_profile', {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            alert('Профиль успешно сохранен!');
        } else {
            alert('Ошибка при сохранении профиля.');
        }
    } catch (error) {
        console.error('Ошибка:', error);
        alert('Ошибка сети.');
    } finally {
        hideLoading();
    }
});

// Поиск анкет
document.getElementById('search-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    showLoading();

    const searchData = {
        city: document.getElementById('search-city').value,
        age_min: parseInt(document.getElementById('search-age-min').value),
        age_max: parseInt(document.getElementById('search-age-max').value),
        gender: document.getElementById('search-gender').value,
        height_min: parseInt(document.getElementById('search-height-min').value),
        height_max: parseInt(document.getElementById('search-height-max').value),
        eye_color: document.getElementById('search-eye-color').value,
        hair_color: document.getElementById('search-hair-color').value,
        interests: document.getElementById('search-interests').value,
    };

    try {
        const response = await fetch('/api/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(searchData),
        });

        if (response.ok) {
            const profiles = await response.json();
            displayProfiles(profiles);
        } else {
            alert('Ошибка при поиске анкет.');
        }
    } catch (error) {
        console.error('Ошибка:', error);
        alert('Ошибка сети.');
    } finally {
        hideLoading();
    }
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
            <button onclick="likeProfile(${profile.user_id})">
                <i class="fas fa-heart"></i> Лайк
            </button>
        `;

        profilesList.appendChild(profileCard);
    });
}

// Лайк профиля
async function likeProfile(userId) {
    showLoading();

    try {
        const response = await fetch('/api/like', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ user_id: userId }),
        });

        if (response.ok) {
            alert('Лайк успешно поставлен!');
        } else {
            alert('Ошибка при постановке лайка.');
        }
    } catch (error) {
        console.error('Ошибка:', error);
        alert('Ошибка сети.');
    } finally {
        hideLoading();
    }
}