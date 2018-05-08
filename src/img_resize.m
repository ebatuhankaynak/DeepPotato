Directory = 'buildings20/';
cities = dir(Directory);
numCities = length(cities);
for i = 3:numCities
    city = cities(i).name;
%     savePath = strcat('resize256/', city);
    savePath = 'resize256/';
    mkdir(savePath);
    fullpath = strcat(Directory, city, '/');
    images = dir(fullpath);
    numImages = length(images);
    for j = 3:numImages
        filename = images(j).name;
        filename = fullfile(fullpath, filename);
        img = imread(filename);
        reImg = imresize(img, [256 256]);
%         saveName = strcat(city, num2str(j - 2), '.png');
        saveName = strcat(num2str(20 * (i - 3) + (j - 2)), '.png');
        imwrite(reImg, strcat(savePath, '/', saveName));
    end
end
