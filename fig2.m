% figure(1)
set(subplot(1, 2, 1), 'Position', [.1 .35 .4 .4])
x = kernelSizes;
y1 = features(1, 1:size(kernelSizes, 2));
plot(x, y1, 'Color', colorDarker(3,:), 'LineWidth', 1.5)
ylim([860 1520])
yticks([900 1200 1500])
ylabel('Mean features extracted per image')
ax = gca;
ax.XDir = 'reverse';
xlim([0 9])
xticks([0 1 3 5 7 9])

set(subplot(1, 2, 2),'Position',[.5 .35 .4 .4])
y2 = features(2, 1:size(kernelSizes, 2));
plot(x, y2, 'Color', colorDarker(3,:), 'LineWidth', 1.5)
ylim([860 1520])
xlim([0 9])
xticks([0 1 3 5 7 9])
set(gca,'ytick',[], 'ycolor', 'k')
xlabel('Kernel size: \leftarrow Low Pass, High Pass \rightarrow')

figure(2)
x = resPercentage;
y1 = features(3, 1:size(resPercentage, 2));
plot(x, y1, 'Color', colorDarker(3,:), 'LineWidth', 1.5)
ylim([500 1310])
yticks([500 700 900 1100 1300])
ylabel('Mean features extracted per image')
xlabel('% of original resolution')
xlim([30 100])
xticks([30 50 70 90 100])

figure(3)
x = clipLimit;
y = features(4, 1:size(clipLimit, 2));
plot(x, y, 'Color', colorDarker(3,:), 'LineWidth', 1.5)
ylim([3700 7200])
yticks([4000 5000 6000 7000])
ylabel('Mean features extracted per image')
xlabel('Clip Limit')
xlim([0 3])