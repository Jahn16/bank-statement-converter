### --- Build Stage --- ###

FROM node:20-alpine as build


WORKDIR /app

RUN adduser --disabled-password --gecos '' appuser \
  && chown -R appuser:appuser /app
USER appuser

COPY --chown=appuser:appuser . .

RUN npm install
RUN npm run build

### --- Run Stage --- ###

FROM nginx:stable-alpine

RUN chown -R nginx:nginx /usr/share/nginx/html /var/cache/nginx
USER nginx

COPY --from=build --chown=nginx:nginx /app/dist /usr/share/nginx/html
COPY --chown=nginx:nginx nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl --fail http://localhost/ || exit 1

CMD ["nginx", "-g", "daemon off;"]
